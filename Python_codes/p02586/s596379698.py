import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8, i8, i8, i8[:,:]), cache=True)
def solve(R,C,K,item):
  dp = np.zeros((C+1,4), dtype=np.int64)
  for i in range(1,R+1):
    new_dp = np.zeros((C+1,4), dtype=np.int64)
    #上から移動
    for k in range(4):
      new_dp[:,0] = np.maximum(new_dp[:,0], dp[:,k])
    dp = new_dp
    for j in range(1,C+1):
      #横から移動
      for k in range(4):
        new_dp[j][k] = np.maximum(new_dp[j,k],new_dp[j-1,k])
      #アイテムを取る
      for k in range(2,-1,-1):
        dp[j,k+1] = np.maximum(dp[j,k+1],dp[j,k]+item[i-1][j-1])
  ans = dp[-1].max()
  return ans

R, C, K = map(int, input().split())
item = np.zeros((R,C), dtype=np.int64)
for i in range(K):
  r,c,v = map(int, input().split())
  item[r-1,c-1] = v
print(solve(R,C,K,item))
