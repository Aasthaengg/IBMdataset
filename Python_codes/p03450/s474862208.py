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

N,M = getNM()
graph = [[] for i in range(N)]
for _ in range(M):
  l,r,d = getNM()
  graph[l-1].append((r-1,d))
  graph[r-1].append((l-1,-d))

q = deque([i for i in range(N)])
pos = [None for i in range(N)]
while q:
  x = q.popleft()
  if pos[x] == None:
    pos[x] = 0
  for y,d in graph[x]:
    if pos[y] == None:
      pos[y] = pos[x] + d
      q.appendleft(y)
      continue
    if pos[y] != pos[x] + d:
      print("No")
      exit()

print("Yes")