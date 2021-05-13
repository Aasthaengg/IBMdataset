import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10**9)
mod = 10**9+7

S = s()
N = len(S)
dp = [[0]*13 for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    for j in range(13):
        if S[i] == '?':
            for k in range(10):
                dp[i+1][(10*j+k)%13] = (dp[i+1][(10*j+k)%13]+dp[i][j])%mod
        else:
            x = int(S[i])
            dp[i+1][(10*j+x)%13] = (dp[i+1][(10*j+x)%13]+dp[i][j])%mod
print(dp[N][5])