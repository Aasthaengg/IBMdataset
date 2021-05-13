# n, k = map(int, input())
n = int(input())
heights = list(map(int, input().split()))
heights = [0] + heights
dp = [10**10]*(n+1)
dp[1] = 0
for i in range(1, n+1 - 2):
    dp[i+1] = min(dp[i+1], abs(heights[i+1] - heights[i]) + dp[i])
    dp[i+2] = min(dp[i+2], abs(heights[i+2] - heights[i]) + dp[i])

dp[n] = min(dp[n], dp[n-1] + abs(heights[n] - heights[n-1]))
print(dp[n])

