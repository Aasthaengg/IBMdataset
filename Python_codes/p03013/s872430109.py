import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0
inf = float("inf")

def dpp(n):
    for i in range(2,n+1):
        if a[i] == 0:
            dp[i] = 0
        else:
            dp[i] = dp[i-1]+dp[i-2]
    return dp[n]

N,M = I()
a = [1]*(N +1)
for i in range(M):
    x = k()
    a[x] = 0

dp = [0]*(N+1)
if a[1] == 0:
    dp[1] = 0
    dp[0] = 1
else:
    dp[0] = dp[1] =1

print(dpp(N) % mod)
