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

s = STR()
k = INT()
ans = 0
a = 0
b = 0
if s[0] == s[-1]:
    if len(set(s)) == 1:
        ans = len(s) * k // 2
        print(ans)
        exit()
    for j in range(len(s)):
        if s[0] == s[j]:
            a += 1
        else:
            break
    for j in reversed(range(len(s))):
        if s[-1] == s[j]:
            b += 1
        else:
            break
    ans = a // 2 + b // 2 + (a + b) // 2 * (k - 1)
i = a
ans2 = 0
while i < len(s) - b:
    tmp = 1
    for j in range(i + 1, len(s)):
        if s[i] == s[j]:
            tmp += 1
        else:
            break
    i += tmp
    tmp //= 2
    ans2 += tmp
print(ans + ans2 * k)