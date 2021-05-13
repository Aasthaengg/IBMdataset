import sys
import itertools
sys.setrecursionlimit(1000000000)
from heapq import heapify,heappop,heappush,heappushpop
import math
import collections
import copy

n = int(input())
dp = [0]*(1000001)
dp[0] = 1
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[n])
