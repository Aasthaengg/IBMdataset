h,n=map(int,input().split())
magics=[list(map(int,input().split())) for i in range(n)]

#import numpy as np

#dp = np.full((n+1, h+1), 10**10)
dp=[[10**10 for _ in range(h+1)]for _ in range(n+1)]
dp[0][0]=0
for i in range(0,n):
  damage = magics[i][0]
  cost = magics[i][1]
  for j in range(0,h+1):
    dp[i+1][j] = min( dp[i+1][j], dp[i][j] )

    to = min( j+damage, h )
    dp[i+1][to] = min( dp[i+1][j]+cost, dp[i+1][to] )
                                                 
print(dp[n][h])