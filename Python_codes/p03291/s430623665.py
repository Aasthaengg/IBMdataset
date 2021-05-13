s=input()
import numpy as np
dp=np.zeros((len(s)+1,4),dtype=np.int64)
dp[0][0]=1
mod=10**9+7
for i in range(len(s)):
    if s[i]=='?':
        dp[i+1]=dp[i]*3
        dp[i+1][1:]+=dp[i][:3]
        dp[i+1]%=mod
    else:
        dp[i+1]=dp[i]
        j=ord(s[i])-ord('A')
        dp[i+1][j+1]=(dp[i+1][j+1]+dp[i][j])%mod
print(dp[-1][3])