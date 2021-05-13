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

n, a, b, c, d = rm()
s = rr()
three = '...' in s[max(0, b-2):min(n-1, d+1)]
sha = '##'in s[b-1:d]
sha1 = '##' in s[a-1:c]
if c < d:
    if sha or sha1:
        print('No')
    else:
        print('Yes')
elif not sha and three and not sha1:
    print('Yes')
else:
    print('No')







