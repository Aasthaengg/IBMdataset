'''
Created on 2020/09/15
 
@author: harurun
'''
import sys
pin=sys.stdin.readline
 
N,K=map(int,pin().split())
h=list(map(int,pin().split()))
dp=[0]*N
for i in range(1,N):
  dp[i]=dp[i-1]+abs(h[i-1]-h[i])
  for j in range(1,K+1):
    if i-j>=0:
      dp[i]=min(dp[i],dp[i-j]+abs(h[i-j]-h[i]))
print(dp[N-1])
# print(dp)
#解説AC