INF = 10 ** 20

n, m = map(int, input().split())

lst = list(map(int, input().split()))

dp = [INF for _ in range(n+1)]

dp[0] = 0

for coin in lst:
    for j in range(coin, n+1):
        dp[j] = min(dp[j], dp[j-coin]+1)
print(dp[n])
