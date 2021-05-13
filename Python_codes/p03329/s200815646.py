# dp
# N円を作るのに最も小さい操作回数

import sys
readline = sys.stdin.readline

N = int(readline())

dp = [i for i in range(N + 1)]

for i in range(len(dp)):
  n = 6
  while i + n < len(dp):
    if dp[i + n] > dp[i] + 1:
      dp[i + n] = dp[i] + 1
    n *= 6
  n = 9
  while i + n < len(dp):
    if dp[i + n] > dp[i] + 1:
      dp[i + n] = dp[i] + 1
    n *= 9
print(dp[N])
