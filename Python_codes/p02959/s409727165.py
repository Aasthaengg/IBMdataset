import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.readline().rstrip()
rs = lambda: map(str, sys.stdin.buffer.readline().split())
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n = ri()
a = rl()
b = rl()
cnt = 0
for i in range(n):
  ai = a[i]
  bi = b[i]
  if bi > ai:
    cnt += ai
    bi -= ai
    ai1 = a[i+1]
    if bi > ai1:
      cnt += ai1
      a[i+1] = 0
    else:
      a[i+1] -= bi
      cnt += bi
  else:
    cnt += bi
print(cnt)



