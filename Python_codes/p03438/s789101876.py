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

n = INT()
a = LIST()
b = LIST()
dif = sum(b) - sum(a)
if dif < 0:
    print('No')
    exit()
cnt1 = 0
cnt2 = 0
for i in range(n):
    tmp = b[i] - a[i]
    if tmp > 0:
        cnt2 += (tmp + 1) // 2
    else:
        cnt1 += -tmp
if dif < cnt1 or dif < cnt2:
    print('No')
    exit()
print('Yes')