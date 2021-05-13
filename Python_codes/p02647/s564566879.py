import numpy as np
from numba import njit,i8

@njit(i8[:](i8[:]),cache = True)
def calc(A):
    B = np.zeros_like(A)
    for i in range(len(A)):
        B[max(0,i - A[i])] += 1
        if i + A[i] + 1 < len(A):
            B[i + A[i] + 1] -= 1
    B = np.cumsum(B)
    return B
  
import sys
readline=sys.stdin.readline
  
N,K = map(int,readline().split())
A = np.array(list(map(int,readline().split())))

for i in range(K):
  A = calc(A)
  if A[0] == N and len(set(A)) == 1:
    break
print(*A)
