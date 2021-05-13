#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
import numpy as np
from collections import Counter, defaultdict, deque
from copy import deepcopy
from decimal import Decimal
from math import gcd
from operator import add, itemgetter, mul, xor
def cmb(n,r,mod):
  bunshi=1
  bunbo=1
  for i in range(r):
    bunbo = bunbo*(i+1)%mod
    bunshi = bunshi*(n-i)%mod
  return (bunshi*pow(bunbo,mod-2,mod))%mod
mod = 10**9+7
def I(): return int(input())
def LI(): return list(map(int,input().split()))
def MI(): return map(int,input().split())
def LLI(n): return [list(map(int, input().split())) for _ in range(n)]

n,m = MI()
num = [-1]*(n+1)
num[0] = 0
bool = True
for i in range(m):
    s,c = MI()
    if n != 1 and s == 1 and c == 0:
      bool = False
      break
    if num[s] == -1 or num[s] == c:
        num[s] = c
    else:
        bool = False
        break
if bool:
  for i in range(n+1):
    if num[i] == -1:
      num[i] = 0
    if n > 1 and num[1] == 0:
      num[1] = 1
  ans = num[1:]
  m = map(str, ans)
  print(''.join(m))
else:
    print(-1)
