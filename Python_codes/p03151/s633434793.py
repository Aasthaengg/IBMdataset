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
if sum(a) < sum(b):
    print(-1)
    exit()
dif = [0 for _ in range(n)]
for i in range(n):
    dif[i] = b[i] - a[i]
dif.sort(reverse=True)
cnt = 0
s = 0
for i in range(n):
    if dif[i] > 0:
        cnt += 1
        s += dif[i]
t = 0
for i in reversed(range(n)):
    if t >= s:
        break
    if dif[i] < 0:
        t -= dif[i]
        cnt += 1
print(cnt)