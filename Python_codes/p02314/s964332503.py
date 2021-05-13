n,m = map(int,input().split())
coins = list(map(int,input().split()))

inf = 10 ** 6

dp = [inf] * (n + 1)
dp[0] = 0

for c in range(m):
  for v in range(n + 1):
    if v >= coins[c]:
      dp[v] = min(dp[v - coins[c]] + 1,dp[v])
    else:
      dp[v] = dp[v]
      
print(dp[n])
