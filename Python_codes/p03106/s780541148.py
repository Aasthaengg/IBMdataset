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

a, b, k = rm()
t = math.gcd(a, b)
cnt = 0
for i in range(t, 0, -1):
  if t % i == 0:
    cnt += 1
    if cnt == k:
      print(i)
      exit()
  
    








