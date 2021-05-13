"""dpまじでわからん"""
'''
Created on 2020/08/29

@author: harurun
'''
import sys
N=int(sys.stdin.readline())
h=list(map(int,sys.stdin.readline().split()))
dp=[0]*N

for i in range(1,N):
  if i>=2:
    dp[i]=min(dp[i-1]+abs(h[i-1]-h[i]),dp[i-2]+abs(h[i-2]-h[i]))
  else:
    dp[i]=dp[i-1]+abs(h[i-1]-h[i])
print(dp[N-1])
# print(dp)