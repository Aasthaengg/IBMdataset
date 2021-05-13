import numpy as np
import sys
input = sys.stdin.readline
#actions=[]
N=int(input())
actions=[[int(x) for x in input().split()] for i in range(N)]
dp=np.zeros((N,3),dtype=int)
dp[0]=actions[0]
for i in range(1,N):
  dp[i][0]=max(dp[i-1][1],dp[i-1][2])+actions[i][0]
  dp[i][1]=max(dp[i-1][0],dp[i-1][2])+actions[i][1]
  dp[i][2]=max(dp[i-1][1],dp[i-1][0])+actions[i][2]
print(max(dp[N-1]))