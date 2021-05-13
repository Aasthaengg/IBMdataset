import numpy as np
N,K,Q=map(int,input().split())
A=[int(input()) for i in range(Q)]

if K-Q<=0:
  L=[K-Q for i in range(N)]
  for i in range(Q):
    L[A[i]-1]=L[A[i]-1]+1
  for i in range(N):
    if L[i]>0:
      print('Yes')
    else:
      print('No')
else:
  for i in range(N):
    print('Yes')