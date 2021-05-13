import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product
def input():
    return sys.stdin.readline()[:-1]
def ruiseki(lst):
    return [0]+list(accumulate(lst))
sys.setrecursionlimit(500000)
mod=10007
al=[chr(ord('a') + i) for i in range(26)]
direction=[[1,0],[0,1],[-1,0],[0,-1]]

n,k=map(int,input().split())
h=list(map(int,input().split()))

dp=[float('inf')]*n
dp[0]=0
for i in range(n):
    for j in range(k):
        # nex=i+j+1
        if i+j+1<n:
            dp[i+j+1]=min(dp[i+j+1],dp[i]+abs(h[i]-h[i+j+1]))
    # print(dp)
print(dp[-1])