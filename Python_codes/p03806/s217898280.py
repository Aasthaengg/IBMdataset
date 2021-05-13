import sys
input = sys.stdin.readline
N, a, b = map(int, input().split())
t = []
dp = [[[float("inf")] * (N * 10 + 1) for _ in range(N * 10 + 1)] for _ in range(N + 1)]
dp[0][0][0] = 0
for i in range(N):
  x, y, c = map(int, input().split())
  for j in range(N * 10 + 1):
    for k in range(N * 10 + 1):
      if dp[i][j][k] != float("inf"):
        dp[i + 1][j + x][k + y] = min(dp[i + 1][j + x][k + y], dp[i][j][k] + c)
      dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
res = float("inf")
for j in range(1, N * 10 + 1):
  for k in range(1, N * 10 + 1):
    if j / a == k / b:
      res = min(res, dp[-1][j][k])
if res != float("inf"): print(res)
else: print(-1)