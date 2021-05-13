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
def L(): return list(input().split())
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
mod = 10**9+7

S = i()
time = []

for i in range(S):
    a = l()
    a.reverse()
    time.append(a)

time.sort()

pl = 0

for i in range(S):
    pl += time[i][1]
    if pl > time[i][0]:
        print("No")
        sys.exit()

print("Yes")
