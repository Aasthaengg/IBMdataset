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
cnt = 0
for i in range(1, n-1):
  if li[i-1] < li[i] < li[i+1] or li[i-1] > li[i] > li[i+1]:
    cnt += 1
print(cnt)








