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

n,m=map(int,input().split())
s=list(map(int,input().split()))
t=list(map(int,input().split()))

dp=[[0]*(m+1) for i in range(n+1)]
sumij=[[0]*(m+1) for i in range(n+1)]
for i in range(n):
    for j in range(m):
        if s[i]==t[j]:
            dp[i+1][j+1]=sumij[i][j]+1
        else:
            dp[i+1][j+1]=0
        sumij[i+1][j+1]=(sumij[i][j+1]+sumij[i+1][j]-sumij[i][j]+dp[i+1][j+1])%mod
print((sumij[-1][-1]+1)%mod)
# print(dp)