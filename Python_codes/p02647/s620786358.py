import numpy as np
N,K = map(int,input().split())
A = np.array(input().split(),dtype=int)
I = np.arange(N)
for i in range(K):
  X = np.zeros(N+1,int)
  np.add.at(X,np.maximum(I-A,0),1)
  np.add.at(X,np.minimum(I+A+1,N),-1)
  A = X.cumsum()[:-1]
  if np.all(A==N):
    break
print(*A)