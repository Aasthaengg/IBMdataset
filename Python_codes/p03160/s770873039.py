import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
import collections
from collections import deque 

input = sys.stdin.readline

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))
def _dbg(o):
    print(o, file=sys.stderr)

# ---------------------------------------

N = inp()
h = inpl()

INF = 1001001001

dp = [0] * (N)
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

print(dp[N-1])
