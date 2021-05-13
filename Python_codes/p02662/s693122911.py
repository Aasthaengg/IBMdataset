#import sys
#import numpy as np
#import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect

n,s=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353

dp=[[0]*3001 for _ in range(n+1)]
dp[0][0]=1
res={i for i in range(1,n+1)}
for i in range(1,n+1):
    for j in range(3001):
        if j>=a[i-1] and dp[i-1][j-a[i-1]]!=0:
            dp[i][j]=(2*dp[i-1][j]+dp[i-1][j-a[i-1]])%mod
           
        else:
            dp[i][j]=(2*dp[i-1][j])%mod
ans=0
print(dp[n][s])