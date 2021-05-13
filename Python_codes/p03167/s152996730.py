import sys
import numpy as np
from functools import lru_cache
from collections import deque

#input = sys.stdin.readline
#sys.setrecursionlimit(10 ** 5)

H,W = map(int,input().split())
grid = [list(input()) for i in range(H)]
dp = [[0] * (W + 1) for i in range(H + 1)]
dp[0][0] = 1
mod = (10 ** 9) + 7

for i in range(H):
  for j in range(W):
    if i > 0 or j > 0:
      if grid[i][j] == "#":
        dp[i][j] = 0
      else:
        dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod

print(dp[H - 1][W - 1])
#print(dp)