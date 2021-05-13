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

N = i()
a = l()
b1 = []
b2 = []
for i in range(N):
    if i%2==0:
        b1.append(a[i])
    else:
        b2.append(a[i])
c1 = Counter(b1)
c2 = Counter(b2)
k1,v1 = c1.most_common()[0]
k2,v2 = c2.most_common()[0]
ans = v1+v2
v3 = 0
v4 = 0
if k1 == k2:
    if len(list(c2.values())) > 1:
        v4 = c2.most_common()[1][1]
    if len(list(c1.values())) > 1:
        v3 = c1.most_common()[1][1]
    ans = max(v1+v4,v2+v3)
print(N-ans)