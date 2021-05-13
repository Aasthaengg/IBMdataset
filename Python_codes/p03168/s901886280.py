import numpy as np
n= int(input())
ppp = list(map(float,input().split()))
dp = [0]*(n+1)
dp[0]=1
for p in ppp:
  ndp = [item*(1-p) for item in dp]
  ndp = [ndp[i] if i == 0 else ndp[i]+dp[i-1]*p for i in range(n+1)]
  dp = ndp
print(sum(dp[n//2+1:]))