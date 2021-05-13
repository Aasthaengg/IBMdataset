import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
import heapq
#import math
import itertools
import numpy as np
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))

s = ri()
dp = [1]*max(4,(s+1))
for i in range(3):
    dp[i]=0
dp[3]=1
#[0,0,1,1,1,2,3,]
#a[i] = a[i-3]+...+a[0]
#     = a[i-3]+a[i-1]
for i in range(4,s+1):#3-7
    dp[i] = dp[i-3]+dp[i-1]

print(dp[s]%MOD)