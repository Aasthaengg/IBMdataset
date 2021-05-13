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
from heapq import heapify, heappop, heappush
from math import sqrt
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

N, K = getNM()
A = getList()

A.sort(reverse = True)

# x以上になるペアが何個あるか
def cnt(x):
    r = 0
    ans = 0
    list_num = [0] * N
    for i in range(N - 1, -1, -1):
        while r < N and A[r] + A[i] >= x:
            r += 1
        list_num[i] = r
        ans += r

    return [ans, list_num]

ng = 0
ok = 2 * (10 ** 6)

while ok - ng > 1:
    mid = (ok + ng) // 2
    if cnt(mid)[0] <= K:
        ok = mid
    else:
        ng = mid

# 境界がわかったら
imos = [0] + copy.deepcopy(A)
for i in range(N):
    imos[i + 1] += imos[i]

ans = 0
plus = cnt(ok)[1]

# cntから得た情報を元に上から順番に足していく
for i in range(N):
    ans += (A[i] * plus[i]) + imos[plus[i]]
# 合計がngになるペアを足りない分K - sum(plus)個足す
ans += ng * (K - sum(plus))
print(ans)