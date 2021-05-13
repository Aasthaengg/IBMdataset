import numpy as np
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n=int(input())
p=list(map(float,input().split()))

dp=np.zeros(n+1)
dp[0]=1
for i in range(n):
      dp[1:]=dp[1:]*(1-p[i])+dp[:-1]*p[i]
      dp[0]=dp[0]*(1-p[i])
print(np.sum(dp[1+n//2:]))