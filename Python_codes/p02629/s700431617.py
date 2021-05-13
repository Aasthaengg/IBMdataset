import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
import functools
def v(): return input()
def k(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
cnt = 0
ans = 0
inf = float("inf")

n = k() - 1
i = 1
s = 26

while n >= s:
    n -= s
    s *= 26
    i += 1

lst = []
for j in range(i):
    lst.append(n % 26)
    n //= 26

for j in lst[::-1]:
    print(chr(j + ord('a')), end='')
