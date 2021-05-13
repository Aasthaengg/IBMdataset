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
al = "abcdefghijklmnopqrstuvwxyz"

import string
s = v()

if s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()

lis =list(string.ascii_lowercase)
nlis = [0]*26

for i in s:
    t = lis.index(i)
    nlis[t] += 1

if sum(nlis) != 26:
    for i in range(26):
        if nlis[i] == 0:
            print(s+lis[i])
            break
else:
    for i in range(25, -1, -1):
        for j in lis:
            if s[i] < j and j not in s[:i]:
                print(s[:i] + j)
                exit()
