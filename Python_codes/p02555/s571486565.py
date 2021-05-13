import os
import sys
import math
import heapq
from decimal import *
from io import BytesIO, IOBase
from collections import defaultdict, deque

def r():
    return int(input())
def rm():
    return map(int,input().split())
def rl():
    return list(map(int,input().split()))

'''D Redistribution'''
mod=10**9+7
n = r()
ans = [0]*(n+1)
dp = [0]*(n+1)
ans[0]=1
dp[0]=1
if n>=1:
    dp[1]=1
if n>=2:
    dp[2]=1
for i in range(3,n+1):
    ans[i]=dp[i-3]
    dp[i]=(dp[i-1]+ans[i])%mod
print(ans[-1])