import sys
readline = sys.stdin.readline

# dp[i][j] = i個目までのコインで、表の個数がj個である確率
# dp[i][j] = dp[i - 1][j] * (1 - P[i]) + dp[i - 1][j - 1] * P[i]
# dp[0][0] = 1 # 0個目までのコインで、表の個数が0個である確率は1

N = int(readline())
P = list(map(float,readline().split()))

dp = [[0] * (N + 1) for i in range(N + 1)]
dp[0][0] = 1
for i in range(len(P)):
  for j in range(i + 2):
    if j - 1 >= 0:
      dp[i + 1][j] = dp[i][j] * (1 - P[i]) + dp[i][j - 1] * P[i]
    else:
      dp[i + 1][j] = dp[i][j] * (1 - P[i])
  
ans = 0
for i in range((N // 2) + 1, len(dp[-1])):
  ans += dp[-1][i]
  
print(ans)