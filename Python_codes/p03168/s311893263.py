N = int(input())
P = [0] + list(map(float, input().split()))
dp = [[0.0 for j in range(N+1)] for i in range(N+1)]
dp[0][0] = 1.0
for i in range(1, N+1):
  for j in range(0, N+1):
    if j > 0:
      dp[i][j] = (1-P[i]) * dp[i-1][j] + P[i] * dp[i-1][j-1]
    else:
      dp[i][j] = (1-P[i]) * dp[i-1][j]
ans = 0.0
for j in range(N+1):
  if j * 2 > N:
    ans += dp[N][j]
print(ans)