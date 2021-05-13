import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = []
for _ in range(N):
  x, y, z = map(int, input().split())
  a.append((x, y, z))
res = -float("inf")
for k in range(8):
  dp = [[-float("inf")] * (M + 1) for _ in range(N + 1)]
  for i in range(N):
    dp[i][0] = 0
    x, y, z = a[i]
    x *= (-1) ** ((k & 1 == 1))
    y *= (-1) ** ((k & 2 == 2))
    z *= (-1) ** ((k & 4 == 4))
    #print(k, x, y, z)
    for j in range(M + 1):
      if dp[i][j] == -float("inf") and (j > 0): continue
      dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
      if j < M:
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x + y + z)
  #print(dp)
  res = max(res, dp[-1][-1])
print(res)