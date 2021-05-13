import numpy as np

n = int(input())
p = list(map(float, input().split()))
index = n//2 + 1

dp = np.zeros((n+1, n+1))
dp[0][0] = (1-p[0])
dp[0][1] = p[0]

for i in range(1, n):
    dp[i] = (1-p[i]) * dp[i-1]
    dp[i][1:] += p[i] * dp[i-1][:-1]

print(sum(dp[n-1][n//2 + 1:]))