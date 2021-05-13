#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect
h,n=map(int,input().split())
inf=10**9
ab = [map(int, input().split()) for _ in range(n)]
a,b=[list(i) for i in zip(*ab)]
dp=[[inf]*(h+1) for _ in range(n+1)]
dp[0][0]=0
for i in range(n):
    for j in range(h+1):
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
        dp[i+1][min(h,j+a[i])]=min(dp[i+1][min(h,j+a[i])],dp[i+1][j]+b[i])
print(dp[-1][-1])