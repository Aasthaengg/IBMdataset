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

h, w = MAP()
a = [LIST() for _ in range(h)]
ans = []
for i in range(h):
    if i % 2 == 0:
        for j in range(w):
            if a[i][j] % 2 == 1:
                y = i
                x = j + 1
                if x >= w:
                    y += 1
                    x = w - 1
                if y < h:
                    a[y][x] += 1
                    ans.append([str(i + 1), str(j + 1), str(y + 1), str(x + 1)])
    else:
        for j in reversed(range(w)):
            if a[i][j] % 2 == 1:
                y = i
                x = j - 1
                if x < 0:
                    y += 1
                    x = 0
                if y < h:
                    a[y][x] += 1
                    ans.append([str(i + 1), str(j + 1), str(y + 1), str(x + 1)])
print(len(ans))
for i in range(len(ans)):
    print(' '.join(ans[i]))