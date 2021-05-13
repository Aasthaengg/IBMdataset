import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
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

mod = 10**9 + 7

H, W = inpl()
a = []
for i in range(H):
    a.append(input().strip())

dp = [[0] * (W+1) for i in range(H+1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        if a[i][j] == "#":
            continue
        for x, y in ((1, 0), (0, 1)):
            dp[i+x][j+y] += dp[i][j]
            dp[i+x][j+y] %= mod

print(dp[H-1][W-1])