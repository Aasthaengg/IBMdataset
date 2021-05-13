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

n, a, b = MAP()
h = [INT() for _ in range(n)]
ad = a - b
l = 1
r = 10 ** 9
while r - l > 1:
    c = (r + l) // 2
    cnt = 0
    for i in range(n):
        cnt += (max(h[i] - b * c, 0) + ad - 1) // ad
    if c > cnt:
        r = c
    else:
        l = c
ans = inf
for i in range(l, r + 1):
    cnt = 0
    for j in range(n):
        cnt += (max(h[j] - b * i, 0) + ad - 1) // ad
    ans = min(ans, max(i, cnt))
print(ans)
