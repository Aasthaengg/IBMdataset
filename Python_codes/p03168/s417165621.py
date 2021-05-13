import numpy as np

n = int(input())
p = list(map(float, input().split()))

dp = np.zeros(n+1)
dp[0] = 1

for i in range(1, n+1):
    dp[1:] = dp[:-1]*p[i-1]+dp[1:]*(1-p[i-1])

print(dp[(n+1)//2])
