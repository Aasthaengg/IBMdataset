import numpy as np
N,M = map(int,input().split())
A = (N+2)*[0]

for m in range(M):
  L,R = map(int,input().split())
  A[L]+=1
  A[R+1]-=1

A = np.cumsum(A)
print(sum(a==M for a in A))