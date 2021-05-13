n = int(input())
p = [float(x) for x in input().split()]

dp = [[0]*(i+2) for i in range(n)]
dp[0][0] = 1-p[0]
dp[0][1] = p[0]

for i in range(1, n):
  for j in range(i+2):
    if j == 0:
      dp[i][j] = dp[i-1][j]*(1-p[i])
      continue
    if j == i+1:
      dp[i][j] = dp[i-1][j-1]*p[i]
      continue
    dp[i][j] = dp[i-1][j-1]*p[i]+dp[i-1][j]*(1-p[i])
ans = 0
for i in range(n//2+1, n+1):
  ans += dp[n-1][i]
print(ans)