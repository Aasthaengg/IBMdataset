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

_, x = rm()
li = rl()
cnt = 0
d = 0
for i in li:
  d += i
  if d <= x:
    cnt += 1
print(cnt + 1)





