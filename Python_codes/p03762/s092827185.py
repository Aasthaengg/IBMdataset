import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
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

n,m = MAP()
x = LIST()
y = LIST()
xsum = 0
for i in range(n):
    xsum -= (n - 1 - i)* x[i]
    xsum += i * x[i]
    xsum %- mod
ysum = 0
for i in range(m):
    ysum -= (m - 1 - i)* y[i]
    ysum += i * y[i]
    ysum %= mod
print(xsum * ysum % mod)
