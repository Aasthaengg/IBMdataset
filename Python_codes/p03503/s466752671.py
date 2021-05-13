import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate, combinations_with_replacement
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
dx = [0, 1, 0, -1, 1, -1, -1, 1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]
debugmode = True

n = INT()
f = [LIST() for _ in range(n)]
p = [LIST() for _ in range(n)]

def func(i, arr):
    if i == 10:
        if sum(arr) == 0:
            return -inf
        pp = 0
        for i in range(n):
            cnt = 0
            for j in range(10):
                if arr[j] == 1 and f[i][j] == 1:
                    cnt += 1
            pp += p[i][cnt]
        return pp
    tmp = deepcopy(arr)
    tmp[i] = 1
    return max(func(i + 1, arr), func(i + 1, tmp))

print(func(0, [0 for _ in range(10)]))

