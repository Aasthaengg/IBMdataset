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

a, b = rm()
if a in [4, 6, 9, 11] and b in [4, 6, 9, 11] or a in [1, 3, 5, 7, 8, 10, 12] and b in [1, 3, 5, 7, 8, 10, 12]:
  print('Yes')
else:
  print('No')







