H,W=map(int,input().split())
#G=[[-1 if input() else 0 for i in range(W)] for _ in range(H)]
MOD=10**9+7
#リストver
dp=[[-1]*W for _ in range(H)]
for i in range(H):
    s=input()
    for j in range(W):
        if s[j]=='#':
            dp[i][j]=0
dp[0][0]=1

'''
#numpy ver
import numpy as np
dp=np.array([list(input()) for _ in range(H)])

dp=np.where(dp=='.',-1,dp)
dp=np.where(dp=='#',0,dp)

dp[0][0]=1
'''
for i in range(H):
    for j in range(W):
        if dp[i][j]==-1:
            if i>0 and j>0:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
            elif i>=1 and j==0:
                dp[i][j]=dp[i-1][j]
            elif i==0 and j>=1:
                dp[i][j]=dp[i][j-1]

print(dp[H-1][W-1]%MOD)