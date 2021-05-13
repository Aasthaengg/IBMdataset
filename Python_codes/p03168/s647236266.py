# input
N = int(input())
p = list(map(float, input().split()))

# dp[i][j] = i回目にコインを投げたとき、面がj個になっている確率
dp = [[0] * (N + 1) for i in range(N + 1)]

dp[0][0] = 1
for i in range(1, N + 1):
  for j in range(N + 1):
    if j - 1 < 0:
      dp[i][j] = dp[i - 1][j] * (1 - p[i - 1])
    else:
      dp[i][j] = dp[i - 1][j - 1] * p[i - 1] + dp[i - 1][j] * (1 - p[i - 1]) # 裏が出てj+1個になる確率と表が出てj+1個になる確率

ans = 0
for i in range(int(N / 2) + 1, N + 1):
  ans += dp[N][i]

print(ans)