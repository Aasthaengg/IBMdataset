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

n,a,b = I()

if (n == 1) and (a == b):
    print(1)
    sys.exit()

if (n == 1) or (a > b):
    print(0)
    sys.exit()

if (n == 2) or (a == b):
    print(1)
    sys.exit()

print((n-2)*(b-a)+1)




"""
n = k()
s = v()

def check(n):
    if 

#コマンドの種類
comand = ["A","B","X","Y"]
p = list(itertools.permutations(comand,2))
for i in range(len(p)):
    p[i] = "".join(p[i])

for i in 
"""