import sys
from collections import *
import heapq
import math
import bisect
from itertools import permutations,accumulate,combinations,product
from fractions import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]

n,a,b=map(int,input().split())
v=list(map(int,input().split()))

dp=[[[-1,0] for j in range(n+1)] for i in range(n+1)]

dp[0][0]=[0,1]
# print(dp)
for i in range(n):
    for j in range(n):
        if dp[i][j][0]==-1:
            continue
        if dp[i][j][0]==dp[i+1][j][0]:
            dp[i+1][j][1]+=dp[i][j][1]

        if dp[i][j][0]>dp[i+1][j][0]:
            dp[i+1][j]=dp[i][j][:]
        
        if dp[i][j][0]+v[i]==dp[i+1][j+1][0]:
            dp[i+1][j+1][1]+=dp[i][j][1]
        
        if dp[i][j][0]+v[i]>dp[i+1][j+1][0]:
            dp[i+1][j+1][0]=dp[i][j][0]+v[i]
            dp[i+1][j+1][1]=dp[i][j][1]
# print(dp)
ans=0
for i in range(a,b+1):
    ans=max(ans, dp[-1][i][0]/i)
print(ans)
cnt=0
for i in range(a,b+1):
    if ans==dp[-1][i][0]/i:
        cnt+=dp[-1][i][1]
print(cnt)