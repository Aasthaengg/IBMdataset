import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.readline().split()))
inf = float('inf')
mod = 10**9 + 7

n = ri()
ans = 0
for i in range(105, n+1, 2):
  cnt = 1
  for k in range(3, int(i**0.5)+1, 2):
    if i % k == 0:
      cnt += 1
  if cnt == 4:
    ans += 1
print(ans)










