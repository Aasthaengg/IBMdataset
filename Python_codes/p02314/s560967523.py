n, m = map(int, input().split())
dp = [0]+[float("inf")]*n
for coin in map(int, input().split()):
    for i, j in zip(range(n), range(coin, n+1)):
        dp[j] = min(dp[i]+1, dp[j])
print(dp[n])
