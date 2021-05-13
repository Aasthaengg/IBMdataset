import numpy as np
from numba import njit

N,K = map(int, input().split())

A_list = np.array([0]+list(map(int, input().split())))

@njit
def update(A_list):

  for j in range(min(K,46)):
    new_A=np.zeros(N+2,dtype=np.int64)
    for i in range(1,N+1):
      #print(new_A)
      mi=i-A_list[i]
      ma=i+A_list[i]
      if mi<0:
        mi=0
      if ma>N:
        ma=N
      #new_A[mi:ma+1]+=1
      new_A[mi]+=1
      new_A[ma+1]-=1

    A_list=np.cumsum(new_A)
    #if sum(A_list[1:N+1])==N*N:
    #  return(A_list)    
    #  break
      
  return(A_list)

A_list=update(A_list)
for i in range(1,N+1):
  print(A_list[i],end=" ")
