import pickle, MWMOTE, random, math
import matplotlib.pyplot as plt 
import numpy as np
# def load_data(path):
#   data_X = []
#   data_Y = []
#   with open(path, 'r') as f:
#     for line in f.readlines():
#       line = line.rstrip().split(" ")
#       data_Y.append(int(line[0]))
#       instance = [0 for i in range(14)]
#       for i in line[1:]:
#         tmp = i.split(':')
#         instance[int(tmp[0])] = float(tmp[1])
#       data_X.append(instance)
  
#   return (data_X,data_Y)


def example():
  N = 5000
  X = []
  Y = [1 for i in range(N)]
  
  for i in range(N):
    X.append([random.uniform(0, 10),random.uniform(0, 10)])
    
  for i, j in enumerate(X):
    if math.hypot(j[0], j[1]) < 5 or math.hypot(j[0]-10, j[1]-10) < 2:
      Y[i] = -1
    if random.random() < 0.01:
      Y[i] = -Y[i]
  return X,Y

if __name__ == '__main__':
  # with open('./heart_scale.pickle', 'r') as f:
  #   X,Y = pickle.load(f)
  X,Y = example()

  X_p = []
  X_n = []
  for i, j in enumerate(Y):
    if j==-1:
      X_n.append(X[i])
    else:
      X_p.append(X[i])
 
  x = np.array(X_p)
  y = np.array(X_n)
 
  plt.plot(x[:,0], x[:,1], 'og', ms = 5)
  plt.plot(y[:,0], y[:,1], 'ob', ms = 5)
  
  

  X_g, Y_g = MWMOTE.MWMOTE(X, Y, 1000)
  z = np.array(X_g)
  plt.plot(z[:,0], z[:,1], 'or', ms = 5)
  plt.show()  