import numpy as np
n=int(input())

dp=[float("inf")]*(n+1)
dp[0]=0

for i in range(1,n+1):
  dp[i]=min(dp[i],dp[i-1]+1)
  for j in range(1,n+1):
    if i-6**j<0: break
    dp[i]=min(dp[i],dp[i-6**j]+1)
    if i-9**j<0: continue
    dp[i]=min(dp[i],dp[i-9**j]+1)
  #print("debug:",i,",",dp[i])

print(dp[n])