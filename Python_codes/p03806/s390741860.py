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

n,ma,mb=map(int,input().split())
abc=[list(map(int,input().split())) for i in range(n)]
dp=[[[float('inf')]*(400+1) for i in range(400+1)] for j in range(n+1)]
dp[0][0][0]=0
for i in range(n):
    a,b,c=abc[i]
    for j in range(400):
        for k in range(400):
            if dp[i][j][k]!=float('inf'):
                dp[i+1][j+a][k+b]=min(dp[i+1][j+a][k+b],dp[i][j][k]+c)
                dp[i+1][j][k]=min(dp[i+1][j][k],dp[i][j][k])
ans=float('inf')
now=[ma,mb]
while 1:
    a,b=now
    ans=min(ans,dp[n][a][b])
    if a+ma>400 or b+mb>400:
        break
    now=[a+ma,b+mb]
if ans==float('inf'):
    print(-1)
else:
    print(ans)