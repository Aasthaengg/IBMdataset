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
l = 0
r = n - 1
print(l, flush=True)
ltmp = STR()
if ltmp == 'Vacant':
    exit()
print(r, flush=True)
rtmp = STR()
if rtmp == 'Vacant':
    exit()
for i in range(2, 20):
    c = (l + r) // 2
    print(c, flush=True)
    tmp = STR()
    if tmp == 'Vacant':
        exit()
    if c % 2 == l % 2:
        if tmp == ltmp:
            l = c
            ltmp = tmp
        else:
            r = c
    else:
        if tmp == ltmp:
            r = c
        else:
            l = c
            ltmp = tmp