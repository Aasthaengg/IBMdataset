import bisect
import copy
import heapq
import math
import sys
from collections import *
from itertools import accumulate, combinations, permutations, product
# from math import gcd
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n=int(input())
p=list(map(float,input().split()))

dp=[defaultdict(float) for i in range(n)]

dp[0][1]=p[0]
dp[0][-1]=1-p[0]
# print(dp)
for i in range(n-1):
    for j in range(-i-1,i+2):
        # print(i,j)
        if j==0:
            dp[i+1][1]+=dp[i][0]*p[i+1]
            dp[i+1][-1]+=dp[i][0]*(1-p[i+1])
        else:
            dp[i+1][j+1]+=dp[i][j]*p[i+1]
            dp[i+1][j-1]+=dp[i][j]*(1-p[i+1])
ans=0.0
for i in range(n):
    ans+=dp[-1][i+1]
# print(dp)
# print(dp[0])
# print(dp[-1])
print(ans)