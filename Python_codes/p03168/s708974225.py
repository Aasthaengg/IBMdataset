import numpy as np

n = int(input())
p = list(map(float, input().split()))

dp = np.zeros(n + 1, float)
dp[0] = 1
for e in p:
    dp[1:] += dp[:-1] * e / (1 - e)
    dp *= 1 - e

ans = dp[(n+1)//2:].sum()
print(ans)
