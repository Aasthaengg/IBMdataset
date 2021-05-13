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

n,t=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
dp=[[-1]*t for i in range(n+1)]
dp[0][0]=0
ans=0
for i in range(n):
    a,b=ab[i]
    for j in range(t):
        dp[i+1][j]=max(dp[i][j],dp[i+1][j])
        if dp[i][j]>=0:
            if j+a>=t:
                ans=max(ans, dp[i][j]+b)
            else:
                dp[i+1][j+a]=max(dp[i+1][j+a], dp[i][j]+b)
for i in range(t):
    ans=max(ans, dp[-1][i])
print(ans)
# print(dp)