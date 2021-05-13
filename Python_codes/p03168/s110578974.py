import numpy as np

n = int(input())
ps = list(map(float, input().split()))

dp = [np.zeros(n + 1) for _ in range(n)]

for i, p in enumerate(ps):
    if i == 0:
        dp[i][0] = 1-p
        dp[i][1] = p
    else:
        dp[i][0] = dp[i-1][0] * (1-p)
        dp[i][1:i+1] = dp[i-1][:i] * p + dp[i-1][1:i+1] * (1-p)
        dp[i][i+1] = dp[i-1][i] * p

l = dp[-1]

print(l[len(l)//2:].sum())
