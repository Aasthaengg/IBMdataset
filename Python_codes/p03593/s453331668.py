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

h, w = MAP()
a = ''
for _ in range(h):
    a += STR()
a = list(a)
b = Counter(a)
c = list(set(a))
n4 = 0
n2 = 0
n1 = 0
for i in c:
    if b[i] % 2:
        n1 += 1
    elif b[i] % 4 == 0:
        n4 += 1
    elif b[i] % 2 == 0:
        n2 += 1
if h % 2 and w % 2:#奇数が一個あって良い。2の倍数が5//2*2コあってもよい
    if n1 == 1 and n2 <= h // 2 + w // 2:
        print('Yes')
    else:
        print('No')
elif h % 2:
    if n1 == 0 and n2 <= w // 2:
        print('Yes')
    else:
        print('No')
elif w % 2:
    if n1 == 0 and n2 <= h // 2:
        print('Yes')
    else:
        print('No')
else:
    if n1 == 0 and n2 == 0:
        print('Yes')
    else:
        print('No')