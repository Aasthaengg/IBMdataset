# n:yen, m:coins
n, m = map(int, input().split())

# list of coins
c = list(map(int, input().split()))

dp = [float("inf")] * (n + 1)
dp[0] = 0

for i in range(m):
    for j in range(n + 1):
        if dp[j] >= 0 and j + c[i] <= n:
            dp[j + c[i]] = min(dp[j + c[i]], dp[j] + 1)


print(dp[n])

