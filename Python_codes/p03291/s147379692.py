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

s=input()
dp=[[0]*(len(s)+1) for i in range(4)]
dp[0][0]=1
lst="ABC"
for i in range(len(s)):
    for j in range(3):
        m1=1
        m2=0
        if s[i]=="?":
            m1=3
            m2=1
        
        if lst[j]==s[i]:
            m2=1
        
        dp[j][i+1]+=m1*dp[j][i]
        dp[j+1][i+1]+=m2*dp[j][i]
        dp[j][i+1]%=mod
        
    if s[i]=="?":
        dp[3][i+1]+=3*dp[3][i]
    else:
        dp[3][i+1]+=dp[3][i]
    dp[3][i+1]%=mod

print(dp[-1][-1]%mod)
# print(dp)