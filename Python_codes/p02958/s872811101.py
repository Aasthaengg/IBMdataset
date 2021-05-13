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

n = ri()
li = rl()
li1 = sorted(li)
cnt = 0
for a, b in zip(li, li1):
  if a != b:
    cnt += 1
print('NO' if cnt > 2 else 'YES')










