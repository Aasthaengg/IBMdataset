import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
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

n, t = MAP()
a = LIST()
get = 0
ans = 0
b = [a[0]]
for i in range(1, n - 1):
    if a[i - 1] < a[i] < a[i + 1]:
        continue
    b.append(a[i])
b.append(a[-1])
d = [0 for i in range(len(b) - 1)]
mn = inf
for i in range(len(b) - 1):
    if mn > b[i]:
        mn = b[i]
    d[i] = b[i + 1] - mn
mx = max(d)
print(d.count(mx))
