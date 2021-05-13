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

li = [ri() for _ in range(5)]
lis = [math.ceil(i/10)*10 for i in li]
ans = inf
for i in range(5):
  ans = min(sum(lis[:i])+li[i]+sum(lis[i+1:]), ans)
print(ans)
  
    








