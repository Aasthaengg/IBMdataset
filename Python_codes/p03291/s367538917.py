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
s=input()
n=len(s)
mod=10**9+7
dp=[[0]*(n+1) for _ in range(4)]
dp[0][0]=1
for i in range(n):
    for j in range(4):
        if s[i]=="?":
            dp[j][i+1]+=dp[j][i]*3
        else:
            dp[j][i+1]+=dp[j][i]
    if s[i]=="A" or s[i]=="?":
        dp[1][i+1]+=dp[0][i]
    if s[i]=="B" or s[i]=="?":
        dp[2][i+1]+=dp[1][i]
    if s[i]=="C" or s[i]=="?":
        dp[3][i+1]+=dp[2][i]
    for j in range(4):
        dp[j][i+1]%=mod
print(dp[3][-1])