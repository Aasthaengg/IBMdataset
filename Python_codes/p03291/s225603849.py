from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)

S = input()
l = len(S)
d = {"A":1,"B":2,"C":3}

dp = [0 for _ in range(4)]
dp[0] = 1
for i in range(l):
    if S[i] == "?":
        dp = [dp[0]*3,dp[1]*3+dp[0],dp[2]*3+dp[1],dp[3]*3+dp[2]]
        for j in range(4):
            dp[j] %= mod
    else:
        j = d[S[i]]
        dp[j] += dp[j-1] % mod

print(dp[3]%mod)