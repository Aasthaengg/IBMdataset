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
from operator import mul
from functools import reduce
from bisect import bisect_left, bisect_right

import sys
sys.setrecursionlimit(1000000000)
mod = 10 ** 9 + 7


#############
# Main Code #
#############

"""
Z algorithm
def Z(s):
    n = len(s)
    z = [0] * n
    z[0] = n

    L, R = 0, 0
    for i in range(1, n):
        if i >= R:
            L = R = i
            # 一致が続く限り伸ばす
            while(R < n and s[R - L] == s[R]):
                R += 1
            # LCAを書き込む
            # 頭から一致しない場合はR - L = i - i = 0
            z[i] = R - L
        # 全て利用できる場合
        elif z[i - L] < R - i:
            z[i] = z[i - L]
        # 一部利用できる場合
        else:
            L = i
            while(R < n and s[R - L] == s[R]):
                R += 1
            z[i] = R - L
    return z

# [5, 0, 3, 0, 1]
#print(Z('ababa'))

N = getN()
S = input()
ans = 0
for i in range(N):
    z = Z(S[i:])
    k = len(z)
    for j in range(k):
        # '' と 'ababa'
        # 'a' と 'baba'
        # 'ab' と 'aba'
        # ans は j('', 'a', 'ab')の長さ以上にならない（ダブらないため）
        ans = max(ans, min(j, z[j]))
print(ans)
"""

# Rolling hash
N = getN()
S = list(map(ord, list(input())))
# 適当
base = 1234
power = [1] * (N + 1)
# 部分文字列を数字に
for i in range(1, N + 1):
    power[i] = power[i - 1] * base % mod

def check(m):
    if N - m < m:
        return False
    res = 0
    for i in range(m):
        res += S[i] * power[m - i - 1]
        res %= mod
    dic = {res: 0}
    for i in range(N - m):
        res = ((res - S[i] * power[m - 1]) * base + S[i + m]) % mod
        if res in dic.keys():
            index = dic[res]
            if index + m <= i + 1:
                return True
        else:
            dic[res] = i + 1
    return False

ok = 0
ng = N + 1
while ng - ok > 1:
    mid = (ok + ng) // 2

    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)