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

# 操作後のAの要素全てが因数にkを持つ

# 好きな回数操作を行えるとすると、Aの要素全てに因数kを持たせることができるか？
# 操作前と操作後とではAの総和は変わらない → A = akとするとa個のkをN個の要素に配分する
# ことでAの要素全てに因数kを持たせることができる。
# 好きな回数操作を行える、操作後のAの全ての要素を割り切る正の整数は、sum(A)の約数になる

def make_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # √nで無い数についてもう一個プラス
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# K回以下の操作の条件付きでも題意を満たすか
# alta % kをし、あまりが小さい順にソートする
# 前からi番目までをプラス、i + 1番目以降をマイナスにする
# どちらか大きい方がK以下なら条件を満たす

def judger(x):
    alta = [i % x for i in A]
    alta.sort()
    alta_b = [x - i for i in alta]
    # 前からi番目までプラスにする
    imos_f = copy.deepcopy(alta)
    # 前からi + 1番目以降をマイナスにする
    imos_b = copy.deepcopy(alta_b)

    for i in range(N - 1):
        imos_f[i + 1] += imos_f[i]
        imos_b[-i - 2] += imos_b[-i - 1]

    # 全部マイナス、全部プラスの場合
    imos_f.insert(0, 0)
    imos_b.append(0)

    ans = float('inf')
    for i in range(N + 1):
        ans = min(ans, max(imos_f[i], imos_b[i]))

    return ans

for i in make_divisors(sum(A))[::-1]:
    if judger(i) <= K:
        print(i)
        break