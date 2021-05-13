import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
S = input()
cnt = Counter(S)
n = len(S)

if n == 1:
    print("YES")
    exit()
elif n == 2:
    if S[0] != S[-1]:
        print("YES")
    else:
        print("NO")
    exit()

ok = False
x = list(cnt.values())
if len(x) < 3:
    print("NO")
    exit()
mn = min(x)
for i in range(3):
    x[i] -= mn
x = sorted(x)
if x[1] <= 1 and x[2] <= 1:
    ok = True

if ok:
    print("YES")
else:
    print("NO")