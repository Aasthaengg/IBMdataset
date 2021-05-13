import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n = ri()
a = rl()
cnt = 0
for i in range(n-1):
    if a[i] == a[i+1]:
        a[i+1] = -1
        cnt += 1
print(cnt)

