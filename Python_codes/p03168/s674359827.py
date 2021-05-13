import numpy as np
n= int(input())
ppp = list(map(float,input().split()))
dp = np.array([0.0]*(n+1),dtype=np.float64)
dp[0]=1
for p in ppp:
  ndp = dp*(1-p)
  ndp[1:] += dp[:-1]*p
  dp = ndp
print(sum(dp[n//2+1:]))