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

h,w,a,b = MAP()
if a > w // 2 or b > h // 2:
    print('No')
    exit()
ans = [['0' for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if (i < b and j < a) or (i >= b and j >= a):
            ans[i][j] = '1'
for i in range(h):
    print(''.join(ans[i]))