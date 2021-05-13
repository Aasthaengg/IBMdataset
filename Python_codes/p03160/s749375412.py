import numpy as np

N = int(input())
heights = [int(i) for i in input().split()]

dp = np.full((N), np.Inf)

dp[0] = 0
dp[1] = abs(heights[1] - heights[0])


for i in range(2, N):
    dp[i] = min(
        dp[i-2] + abs(heights[i] - heights[i-2]),
        dp[i-1] + abs(heights[i] - heights[i-1]),
    )
    

print(int(dp[N-1]))
