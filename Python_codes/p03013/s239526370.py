import bisect, copy, heapq, math
from math import inf
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
def celi(a,b):
    return -(-a//b)
sys.setrecursionlimit(5000000)
mod=pow(10,9)+7
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,m=map(int,input().split())
a=[int(input()) for i in range(m)]

dic={}
for i in range(m):
    dic[a[i]]=1
dp=[0]*(n+2)

dp[0]=1
for i in range(n):
    if i in dic:
        continue
    dp[i+1]+=dp[i]
    dp[i+2]+=dp[i]
    dp[i+1]%=mod
    dp[i+2]%=mod
print(dp[-2])