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

n, l = rm()
li = np.arange(n) + l
if l > 0:
  print(sum(li[1:]))
elif l <= -n:
  print(sum(li[:-1]))
else:
  print(sum(li))







