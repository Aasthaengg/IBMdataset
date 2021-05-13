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
n=int(input())
a=[0]*14
a[0]=1
a[8]=9
for i in range(1,8):
    a[i]=a[i-1]*6
for i in range(9,14):
    a[i]=a[i-1]*9
inf=10**6
dp=[[inf]*(n+1) for _ in range(15)]
dp[0][0]=0
for i in range(14):
    for j in range(n+1):
        dp[i+1][j]=min(dp[i][j],dp[i+1][j])
        if j+a[i]<n+1:
          dp[i+1][j+a[i]]=min(dp[i+1][j]+1,dp[i+1][j+a[i]])
print(dp[-1][-1])