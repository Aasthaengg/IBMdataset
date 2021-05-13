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

s = ri()
li = [s]
cnt = 1
while True:
  if s&1 == 1:
    s = 3*s + 1
  else:
    s = s//2
  cnt += 1
  if s not in li:
    li.append(s)
  else:
    print(cnt)
    exit()








