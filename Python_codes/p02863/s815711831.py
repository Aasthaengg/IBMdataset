import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8,i8,i8[:,:]), cache=True)
def main(N,T,A):
  dp = np.zeros(T+1, np.int64)
  for i in range(N):
    for t in range(T-1,-1,-1):
      u = min(T,t+A[i,0])
      dp[u] = max(dp[u],dp[t]+A[i,1])
  ans = dp[-1]
  return ans

N, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
A = np.array(sorted(A),np.int64)
print(main(N,T,A))