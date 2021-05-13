import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10

# from heapq import heappush, heappop, heapify
# import math
# from math import gcd
# import itertools as it
# import collections
# from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _debug(obj):
    print(obj, file=sys.stderr)

# ---------------------------------------

mod = 998244353

N, K = inpl()
left, right = [0] * K, [0] * K
for i in range(K):
    left[i], right[i] = inpl();

dp = [0] * (N + 1) 
dp[1] = 1
wa = [0] * (N + 1)
wa[1] = 1

for i in range(2, N + 1):
    for k in range(K):
        dp[i] += wa[max(0, i - left[k])] - wa[max(0, i - right[k] - 1)]
        dp[i] %= mod
    wa[i] = (wa[i-1] +  dp[i]) % mod
print(dp[N])

