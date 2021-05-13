import numpy as np

N, K = map(int, input().split())
A = np.array(list(map(int, input().split())))

from numba import jit

@jit
def imos(x):
  global N
  B = np.zeros_like(x)
  for i in range(N):
    p = x[i]
    L = max(i-p, 0)
    R = min(i+p, N-1)
    B[L] += 1
    if R < N-1:
      B[R+1] -= 1
  B = np.cumsum(B)
  return B

for i in range(K):
  if i >= 50:
    break
  A = imos(A)

print(*A)