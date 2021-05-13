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

_, _, x, y = rl()
maxx = max(rm())
miny = min(rm())
if maxx < miny and x<miny and maxx<y:
  print('No War')
else:
  print('War')





