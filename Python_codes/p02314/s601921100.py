INF = float('inf')
n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(n+1):
    for c in coins:
        if i + c <= n:
            dp[i+c] = min(dp[i+c], dp[i] + 1)
print(dp[n])

