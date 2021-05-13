import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N = int(input())
A = Counter(map(int, input().split()))

cand = []
for k, v in A.items():
    if v >= 2:
        cand.append((k, v))
cand = sorted(cand, reverse=True)

ans = 0
if len(cand) == 0:
    ans = 0
elif cand[0][1] >= 4:
    ans = cand[0][0] ** 2
else:
    ans = cand[0][0] * cand[1][0]
print(ans)


