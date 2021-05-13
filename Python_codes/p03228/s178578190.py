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

a, b, k = MAP()
for _ in range(k // 2):
    if a % 2 == 1:
        a -= 1
    b += a // 2
    a //= 2
    if b % 2 == 1:
        b -= 1
    a += b // 2
    b //= 2
if k % 2 == 1:
    if a % 2 == 1:
        a -= 1
    b += a // 2
    a //= 2
print(a, b)