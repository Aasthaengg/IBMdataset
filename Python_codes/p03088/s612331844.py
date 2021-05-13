import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7

n = INT()
dp = [[[[0, 0, 0, 0] for _ in range(4)] for _ in range(4)] for _ in range(n - 2)] #a,c,g,t
arr = [[0, 2, 1], [0, 1, 2], [2, 0, 1]]
for i in range(4):
    for j in range(4):
        for k in range(4):
            if not [i, j, k] in arr:
                dp[0][i][j][k] = 1

arr2 = [[0, 2, 2, 1], [0, 3, 2, 1], [0, 2, 3, 1], [0, 2, 2, 1]]
for nn in range(1, n - 2):
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    if not [i, j, k, l] in arr2 and not [j, k, l] in arr:
                        dp[nn][j][k][l] += dp[nn - 1][i][j][k]
                        dp[nn][j][k][l] %= mod
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[n - 3][i][j][k]
            ans %= mod
print(ans)