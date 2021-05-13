import numpy as np
n=int(input())
p=list(map(float,input().split()))
dp = np.zeros((n+1,n+1),dtype=np.float64)
dp[0][0]=1
for i in range(n):
    dp[i+1][0]=dp[i][0]*(1-p[i])
for i in range(n):
    dp[i+1][1:]=dp[i][1:]*(1-p[i])+dp[i][:-1]*p[i]
print(np.sum(dp[n][n//2+1:]))