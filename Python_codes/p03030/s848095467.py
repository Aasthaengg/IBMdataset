import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def X(): return list(input())
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
def gcd(*numbers): reduce(math.gcd, numbers)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7
count = 0
ans = 0

n = int(input())

r = []

for i in range(n):
    city, score = input().split()
    score = int (score)
    r.append((i+1, city, score))

r.sort(key=lambda x:x[2], reverse=True)
r.sort(key=lambda x:x[1])

for i in range(n):
    print(r[i][0])
