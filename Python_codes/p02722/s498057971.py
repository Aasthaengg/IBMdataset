def getN():
    return int(input())
def getNM():
    return map(int, input().split())
def getList():
    return list(map(int, input().split()))
def getArray(intn):
    return [int(input()) for i in range(intn)]
def input():
    return sys.stdin.readline().rstrip()
def rand_N(ran1, ran2):
    return random.randint(ran1, ran2)
def rand_List(ran1, ran2, rantime):
    return [random.randint(ran1, ran2) for i in range(rantime)]
def rand_ints_nodup(ran1, ran2, rantime):
  ns = []
  while len(ns) < rantime:
    n = random.randint(ran1, ran2)
    if not n in ns:
      ns.append(n)
  return sorted(ns)

def rand_query(ran1, ran2, rantime):
  r_query = []
  while len(r_query) < rantime:
    n_q = rand_ints_nodup(ran1, ran2, 2)
    if not n_q in r_query:
      r_query.append(n_q)
  return sorted(r_query)

from collections import defaultdict, deque, Counter
from sys import exit
from decimal import *
import heapq
import math
from fractions import gcd
import random
import string
import copy
from itertools import combinations, permutations, product
from operator import mul, itemgetter
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7

#############
# Main Code #
#############

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

N = getN()

# 手順としては
# ①　kで出来るだけ割る
# ②　kで引いていく　N = mk + d(d = 1, 2, 3...)とすると,　引いて残る数はm(k - 1) + d
# つまりkで割り切れず、引いても引いても永遠に①に戻ることはない

# N = k ** i * (mk + 1)となるkの数を求める
# i == 0の時
# kがなんであれk ** iは１になるので
# N = mk + 1、つまりN - 1がkの倍数であればそのkは条件を満たす
# N - 1の約数（１以外）が候補

ans = set()
for i in make_divisors(N - 1):
    if i != 1:
        ans.add(i)

# 割れるだけ割る関数
def dividor(x, k):
    if k == 1:
        return 0
    n = x
    while True:
        if n % k == 0:
            n //= k
        else:
            break
    return n

# i >= 1の時
# 候補はNの約数
for prim in make_divisors(N):
    if prim == 1:
        continue
    # Nを割れるだけ割る
    alta = dividor(N, prim)
    if alta == 1:
        ans.add(prim)
        continue
    if alta >= prim and alta % prim == 1:
        ans.add(prim)

print(len(ans))