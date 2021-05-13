import sys
readline = sys.stdin.readline

N = int(readline())
dp = [[0] * 3 for i in range(N + 1)]

for i in range(N):
  works = list(map(int,readline().split()))
  for j in range(3):
    for k in range(3):
      if j == k:
        continue
      dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + works[k])

print(max(dp[-1]))