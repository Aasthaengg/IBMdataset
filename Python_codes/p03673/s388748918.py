import sys
import math
import itertools
import bisect
from copy import copy,deepcopy
from collections import deque,Counter
from decimal import Decimal
def s(): return input()
def i(): return int(input())
def S(): return input().split()
def I(): return map(int,input().split())
def L(): return list(map(int,input().split()))
def l(): return list(map(int,input().split()))
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9
mod = 10**9+7

n = i()
a = l()
deq = deque([])
for i in range(n):
    if i%2 == 0:
        deq.append(a[i])
    else:
        deq.appendleft(a[i])
if n%2 == 1:
    deq.reverse()
print(*deq)