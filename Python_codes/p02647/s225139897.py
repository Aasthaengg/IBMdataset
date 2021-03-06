import sys
import numpy as np
from numba import jit
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, K, *A = map(int, read().split())
 
@jit
def imos(A):
  B = np.zeros_like(A)
  for i,x in enumerate(A):
    a = max(0,i-x)
    b = min(N-1,i+x)
    B[a] += 1
    if b+1 <= N-1:
      B[b+1] -= 1
  B = np.cumsum(B)
  return B
 
for i in range(K):
  if i >= 50:
    break
  A = imos(A)
print(*A)