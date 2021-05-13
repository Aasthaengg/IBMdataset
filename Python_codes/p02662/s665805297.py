import bisect
import copy
import heapq
import math
import sys
import random
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=998244353
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,s=map(int,input().split())
a=list(map(int,input().split()))

dp=[[0]*(s+1) for i in range(n+1)]
dp[0][0]=1

for i in range(n):
    for j in range(s+1):
        dp[i+1][j]+=2*dp[i][j]
        dp[i+1][j]%=mod
        if j+a[i]<=s:
            dp[i+1][j+a[i]]+=dp[i][j]
            dp[i+1][j+a[i]]%=mod

print(dp[n][s])