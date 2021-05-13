n = int(input())
dp = [float('INF')]*(n+1)
dp[0] = 0
for i in range(1, n+1):
    dp[i] = min(dp[i], dp[i-1]+1)
    k = 1
    while i >= 6**k:
        dp[i] = min(dp[i], dp[i-6**k]+1)
        k += 1
    k = 1
    while i >= 9**k:
        dp[i] = min(dp[i], dp[i-9**k]+1)
        k += 1
print(dp[n])