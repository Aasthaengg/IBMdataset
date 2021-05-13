import sys, re, os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, acos, atan, asin, log, log10
from itertools import permutations, combinations, product, accumulate
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
dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
debugmode = False

s = STR()
a = []
i = 0
while i < len(s):
    if s[i] == 'A':
        a.append(0)
        i += 1
    elif i < len(s) - 1 and s[i:i + 2] == 'BC':
        a.append(1)
        i += 2
    else:
        a.append(2)
        i += 1
debug(a)
arr = []
bgn = -1
end = -1
for i in range(len(a)):
    if bgn == -1 and a[i] != 2:
        bgn = i
    if a[i] == 2 and end == -1:
        end = i
        arr.append(a[bgn:end])
        bgn = -1
        end = -1
arr.append(a[bgn:len(a) + 1])
debug(arr)
ans = 0
for b in arr:
    num0 = 0
    for i in b:
        if i == 0:
            num0 += 1
        if i == 1:
            ans += num0
print(ans)
