n, m = map(int, input().split())
dp = [0]*(n+2)
dp[0] = 1
for i in range(m):
  dp[int(input())] = -1

for i in range(n):
  if dp[i] >= 0:
    if dp[i+1] >= 0:
      dp[i+1] += dp[i]
    if dp[i+2] >= 0:
      dp[i+2] += dp[i]

print(dp[n] % 1000000007)