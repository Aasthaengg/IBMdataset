import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
from functools import reduce

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n, m = rm()
cnt = 0
cnt_money = 0
for i in sorted([rl() for _ in range(n)]):
  a, b = i
  if cnt + b < m:
    cnt += b
    cnt_money += a*b
  else:
    cnt_money += (m - cnt) * a
    break
print(cnt_money)
    















