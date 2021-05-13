import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
def debug(*args):
    if debugmode:
        print(*args)
def input(): return sys.stdin.readline().strip()
def STR(): return input()
def INT(): return int(input())
def FLOAT(): return float(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

def digit(n, m):
    n = str(n)
    while m - len(n):
        n = '0' + n
    return n

n, m = MAP()
dp = [[inf for _ in range(2 ** n)] for _ in range(m)]
for i in range(m):
    dp[i][0] = 0
for i in range(m):
    a, b = MAP()
    c = LIST()
    arr = [1 if i + 1 in c else 0 for i in range(n)]
    cnum = 0
    for j in range(n):
        cnum += arr[j] * (2 ** (n - j - 1))
    if i == 0:
        for j in range(1, 2 ** n):
            if (cnum ^ j) & j != 0:
                continue
            dp[i][j] = a
    else:
        for j in range(1, 2 ** n):
            former = (cnum & j) ^ j
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][former] + a)
    debug(dp[i])
if dp[m - 1][2 ** n - 1] >= inf:
    print(-1)
else:
    print(dp[m - 1][2 ** n - 1])
