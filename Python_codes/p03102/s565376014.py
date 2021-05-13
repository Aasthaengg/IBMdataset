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

n, m, c = rm()
b = np.array(rl())
cnt = 0
for _ in range(n):
  a = np.array(rl())
  if np.sum(a*b) > -c:
    cnt += 1
print(cnt)
    








