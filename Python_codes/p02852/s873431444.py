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

n, m = MAP()
s = [int(i) for i in STR()]
flag = False
cnt = 0
for i in range(n + 1):
    if s[i] == 1:
        cnt += 1
    else:
        cnt = 0
    if cnt >= m:
        print(-1)
        exit()
ans = []
hr = n
while hr > 0:
    for i in reversed(range(1, m + 1)):
        if 0 <= hr - i <= n and s[hr - i] == 0:
            ans.append(i)
            hr -= i
            break
ans = list(reversed(ans))
for i in range(len(ans)):
    ans[i] = str(ans[i])
print(' '.join(ans))
