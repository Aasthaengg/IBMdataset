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

def rand_letter(size):
    ascii_original='programing'
    digits_original='01'

    digits='0123456789'
    ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # 好きなものを使ってね
    psuedo = ascii_original

    return ''.join([random.choice(psuedo) for i in range(size)])


S = input()
N_S = len(S)
T = input()
N_T = len(T)

dict_s = defaultdict(int)
dict_order = defaultdict(list)
for i in range(N_S):
    dict_s[S[i]] += 1
    dict_order[S[i]].append(i + 1)

dict_t = defaultdict(int)
for i in range(N_T):
    dict_t[T[i]] += 1

flag = True
for i in dict_t:
    if dict_s[i] == 0:
        flag = False
        break

if not flag:
    print(-1)
    exit()

now = dict_order[T[0]][0]
ans = [dict_order[T[0]][0]]

for i in range(1, N_T):
    index = bisect_right(dict_order[T[i]], now)
    if index == len(dict_order[T[i]]):
        now = dict_order[T[i]][0]
    else:
        now = dict_order[T[i]][index]
    ans.append(now)

cnt = 0
for i in range(1, N_T):
    if ans[i] <= ans[i - 1]:
        cnt += 1
print(cnt * N_S + ans[-1])