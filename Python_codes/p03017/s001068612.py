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
def lcm(a, b): return a * b // gcd(a, b)
sys.setrecursionlimit(10 ** 9)
inf = sys.maxsize
mod = 10 ** 9 + 7
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

n, a, b, c, d = MAP()
s = STR()

dp1 = [inf for _ in range(n + 1)]
dp1[a] = 0
dp1[a - 1] = 0
for i in range(a + 1,c + 1):
    if s[i - 1] == '.':
        dp1[i] = min(dp1[i - 1], dp1[i - 2]) + 1
dp2 = [inf for _ in range(n + 1)]
dp2[b] = 0
dp2[b - 1] = 0
for i in range(b + 1, d + 1):
    if s[i - 1] == '.':
        dp2[i] = min(dp2[i - 1], dp2[i - 2]) + 1

if a < b and c < d or a > b and c > d:
    if dp1[c] < inf and dp2[d] < inf:
        print('Yes')
    else:
        print('No')
else:
    if a > b and c < d:
        a, b = b, a
        c, d = d, c
    flag = False
    for i in range(b, d + 1): #抜かす場所
        if s[i - 2:i + 1] == '...': #抜かせる
            flag = True
            break
    if dp1[c] < inf and dp2[d] < inf and flag:
        print('Yes')
    else:
        print('No')
