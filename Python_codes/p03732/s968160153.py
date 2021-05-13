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

n,w=map(int,input().split())
wv=[list(map(int,input().split())) for i in range(n)]

dp=[[-float('inf')]*101*400 for i in range(n+1)]
dp[0][0]=0

kijun=wv[0][0]
for i in range(n):
    for j in range(101*400):
        if dp[i][j]!=-float('inf'):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])
            ko,a=j//400,j%400
            dp[i+1][(ko+1)*400+a+wv[i][0]-kijun]=max(dp[i+1][(ko+1)*400+a+wv[i][0]-kijun],dp[i][j]+wv[i][1])

ans=0
for i in range(101*400):
    ko,a=i//400,i%400
    if ko*kijun+a<=w:
        ans=max(ans,dp[n][i])
print(ans)