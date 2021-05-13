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

N = getN()
A = getList()

abs_max = A[0]
max_index = 0
ans = []
for i in range(1, N):
    opt = abs(A[i])
    if opt >= abs_max:
        abs_max = opt
        max_index = i

for i in range(N):
    if i != max_index:
        A[i] += A[max_index]
        ans.append([max_index + 1, i + 1])

if A[max_index] >= 0:
    for i in range(1, N):
        A[i] += A[i - 1]
        ans.append([i, i + 1])
else:
    for i in range(N - 1, 0, -1):
        A[i - 1] += A[i]
        ans.append([i + 1, i])

print(len(ans))
for i in ans:
    print(*i)