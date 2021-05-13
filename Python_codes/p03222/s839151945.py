import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

H, W, K = MAP()

dp = [[0]*W for _ in range(H+1)]
dp[0][0] = 1

for i in range(H):
    for j in range(W):
        for S in range(1<<(W-1)):
            for k in range(W-2):
                if (S>>k)&1==1 and (S>>(k+1))&1==1:
                    break
            else:
                if j >= 1 and (S>>(j-1))&1:
                    dp[i+1][j-1] += dp[i][j]
                    dp[i+1][j-1] %= mod
                elif j <= W-2 and (S>>j)&1:
                    dp[i+1][j+1] += dp[i][j]
                    dp[i+1][j+1] %= mod
                else:
                    dp[i+1][j] += dp[i][j]
                    dp[i+1][j] %= mod

print(dp[H][K-1])
