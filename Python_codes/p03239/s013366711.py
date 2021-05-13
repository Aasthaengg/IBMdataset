import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n, t = rm()
min_ = inf
flag = False
for _ in range(n):
  a, b = rm()
  if b <= t:
    min_ = min(min_, a)
    flag = True
if flag:
  print(min_)
else:
  print('TLE')








