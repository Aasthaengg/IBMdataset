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

N, K = getNM()
A = getList()

# 各X xor Aiについて
# 各桁について
# Xにフラグ立つ + Aiにフラグ立たない
# Xにフラグ立たない + Aiにフラグ立つ　の時 2 ** iだけxorの値が増える
# Aの各要素の2 ** iのフラグの合計がn本の時
# Xの2 ** iのフラグを立てるとN - n * 2 ** i、立てないとn * 2 ** i　f(x)の値が増える

# 各桁のフラグが合計何本あるか
flag = [0] * 61
def splitbit(n):
    for i in range(61):
        if n & (1 << i):
            flag[i] += 1
for i in range(N):
    splitbit(A[i])

x = 0
ans = 0
for i in range(60, -1, -1):
    # flag[i] < N - flag[i]ならフラグを立てるほうがお得
    # だがKの制限があり立てたくても立てられないことがある
    # Xの2 ** iのフラグを立ててもXがKを超えないか
    if flag[i] < N - flag[i] and x + 2 ** i <= K:
        # Xにフラグを立てる
        x += 2 ** i
        # f(x)の値が増える
        ans += 2 ** i * (N - flag[i])
    # flag[i] < N - flag[i]だがフラグを立てられない場合 +
    # flag[i] >= N - flag[i]の時
    else:
        ans += 2 ** i * flag[i]

print(ans)