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

a,b,h,m = MI()
min = 60*h+m
pi = math.pi
c = pi/30
d  = pi/360
jisin = (a*math.cos(min*c),a*math.sin(min*c))
hunsin = (b*math.cos(min*d),b*math.sin(min*d))
ans = (jisin[0]-hunsin[0])**2+(jisin[1]-hunsin[1])**2
print(ans**0.5)
