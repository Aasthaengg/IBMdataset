n, k = map(int, input().split())
heights = list(map(int, input().split()))
heights = [0] + heights
dp = [10**10]*(n+1)
dp[1] = 0

for i in range(1, n+1):
    for step in range(1, k+1):
        if (i + step) <= n:
            dp[i+step] = min(dp[i+step], abs(heights[i+step] - heights[i]) + dp[i])
print(dp[n])

