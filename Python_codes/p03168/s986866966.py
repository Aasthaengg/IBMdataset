import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import decimal
from decimal import Decimal
decimal.getcontext().prec = 10

from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

N = inp()
p = [0] + list(map(float, input().split()))
dp = [[0] * (N + 1) for i in range(N + 1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(0, i+1):
        if j > 0:
            dp[i][j] = dp[i-1][j] * (1 - p[i]) + dp[i-1][j-1] * p[i]
        else:
            dp[i][j] = dp[i-1][j] * (1 - p[i])
ans = 0
for j in range(N//2 + 1, N + 1):
    ans += dp[N][j]
print(ans)