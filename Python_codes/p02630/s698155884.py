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

n = k()
a = l()
q = k()
count = [0]*100001
ans = []
an=sum(a)
for i in range(n):
    x = a[i]
    count[x-1] += 1
for i in range(q):
    b,c=I()
    an += (c-b)*count[b-1]
    count[c-1]+=count[b-1]
    count[b-1]=0
    ans.append(an)

for i in ans:
    print(i)
