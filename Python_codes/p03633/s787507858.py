import sys
import math
import itertools
import collections
import heapq
import re
import numpy as np
import fractions
from functools import reduce

rr = lambda: sys.stdin.buffer.readline().rstrip()
rs = lambda: sys.stdin.buffer.readline().split()
ri = lambda: int(sys.stdin.buffer.readline())
rm = lambda: map(int, sys.stdin.buffer.readline().split())
rl = lambda: list(map(int, sys.stdin.buffer.readline().split()))

n = ri()
li = [ri() for _ in range(n)]
ans = 1
for i in li:
  a = fractions.gcd(i, ans)
  ans = ans * i // a
print(ans)
