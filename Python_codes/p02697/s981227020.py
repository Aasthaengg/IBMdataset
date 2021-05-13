import numpy as np
N,M=map(int,input().split())
A=np.arange(M)
B=2*M-1-A
B[:M//2]-=(2*M+1)
A%=N
B%=N
A+=1
B+=1
for i in range(M):
  print(A[i],B[i])