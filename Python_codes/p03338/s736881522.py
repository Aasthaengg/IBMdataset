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

n = ri()
s = rr()
max_cnt = 0
for i in range(1, n-1):
  x = set(s[:i])
  y = set(s[i:])
  max_cnt = max(len(x & y), max_cnt)
print(max_cnt)













