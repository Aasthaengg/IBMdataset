n, w = map(int, input().split())
ws, vs = [], []
for i in range(n):
  wi, vi = map(int, input().split())
  ws.append(wi)
  vs.append(vi)
dp = [[[0] * (3 * i + 1) for i in range(n + 1)] for j in range(n + 1)]
for i in range(n):
  for j in range(n + 1):
    for k in range(3 * j + 1):
      dp[i + 1][j][k] = max(dp[i + 1][j][k], dp[i][j][k])
      if j < n:
        dp[i + 1][j + 1][k + ws[i] - ws[0]] = max(dp[i + 1][j + 1][k + ws[i] - ws[0]],
                                                  dp[i][j][k] + vs[i])
ans = 0
for i in range(n + 1):
  for j in range(3 * i + 1):
    if ws[0] * i + j <= w:
      ans = max(ans, dp[n][i][j])
print(ans)
