#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**7)
import bisect
import heapq
import itertools
import math
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

#bisect.bisect_left(list,key)はlistのなかでkey未満の数字がいくつあるかを返す
#bisect.bisect_right(list, key)はlistのなかでkey以下の数字がいくつあるかを返す
#これを応用することで
#len(list) - bisect.bisect_left(list,key)はlistのなかでkey以上の数字がいくつあるかを返す
#len(list) - bisect.bisect_right(list,key)はlistのなかでkeyより大きい数字がいくつあるかを返す
#これらを使うときはあらかじめlistをソートしておくこと！
n,m,k = MI()
a = LI()
b = LI()
a_cum = [0]
b_cum = [0]
ans = 0
for i in range(1,n+1):
    a_cum.append(a[i-1]+a_cum[i-1])
for i in range(1,m+1):
    b_cum.append(b[i-1]+b_cum[i-1])
for i in range(m+1):
    K = k-b_cum[i]
    if K >= 0:
    #K以下で最大のa_cum[j]を求め出力するのはi+j
      j = bisect.bisect_right(a_cum, K) - 1
      ans = max(ans,i+j)
print(ans)

