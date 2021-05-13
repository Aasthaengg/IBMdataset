import numpy as np
n,k = map(int,input().split())
h = np.array(list(map(int, input().split())))
dp = np.array([np.inf] * n)
dp[0]=0
dp[1]=abs(h[1]-h[0])
for i in range(2,n):
    if i-k > 0:
        dp[i] = min(dp[i-k:i]+abs(h[i]-h[i-k:i]))
    else:
        dp[i] = min(dp[0:i]+abs(h[i]-h[0:i]))
print(int(dp[n-1]))