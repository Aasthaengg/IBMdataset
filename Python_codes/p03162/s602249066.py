'''
Created on 2020/09/15

@author: harurun
'''
import sys
pin=sys.stdin.readline

N=int(pin())
dp=[[0]*3 for _ in [0]*N]

dp[0][0],dp[0][1],dp[0][2]=map(int,pin().split())
for i in range(1,N):
  a,b,c=map(int,pin().split())
  dp[i][0]=max(dp[i-1][1]+a,dp[i-1][2]+a)
  dp[i][1]=max(dp[i-1][0]+b,dp[i-1][2]+b)
  dp[i][2]=max(dp[i-1][0]+c,dp[i-1][1]+c)

print(max(dp[N-1]))
#解説AC