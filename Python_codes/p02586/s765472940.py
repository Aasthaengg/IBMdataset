import sys
import numpy as np
import numba
from numba import njit, b1, i4, i8, f8
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

@njit((i8, i8, i8, i8[:]), cache=True)
def solve(R,C,K,XYV):
  item = np.zeros((R + 1, C + 1), dtype=np.int64)
  for i in range(0, 3 * K, 3):
    x, y, v = XYV[i:i + 3]
    item[x - 1, y - 1] = v
  dp = np.zeros((C+1,4), dtype=np.int64)
  for i in range(R):
    new_dp = np.zeros((C+1,4), dtype=np.int64)
    #上から移動
    for k in range(4):
      new_dp[:,0] = np.maximum(new_dp[:,0], dp[:,k])
    dp = new_dp
    for j in range(1,C+1):
      #横から移動
      for k in range(4):
        new_dp[j,k] = np.maximum(new_dp[j,k],new_dp[j-1,k])
      #アイテムを取る
      for k in range(2,-1,-1):
        dp[j,k+1] = np.maximum(dp[j,k+1],dp[j,k]+item[i,j-1])
  ans = dp[-1].max()
  return ans

R, C, K = map(int, readline().split())
XYV = np.array(read().split(), np.int64)
print(solve(R,C,K,XYV))
