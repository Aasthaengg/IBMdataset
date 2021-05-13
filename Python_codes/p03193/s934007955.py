import numpy as np

param = [int(i) for i in input().split()]
N = param[0]
H = param[1]
W = param[2]

material = np.empty([N,2],dtype=np.int)

for i in range(N):
    material[i,:] = [int(j) for j in input().split()]

count = np.array([material[:,0] >= H, material[:,1] >= W]).T
count = np.all(count==True, axis=1)
count = np.sum(count)
print(count)