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
A = list(map(int, input().split()))
B = list(map(int, input().split()))
sa = sum(A)
sb = sum(B)

if sb > sa:
    print(-1)
    exit()

has_margin = []
need_point = []
for a, b in zip(A, B):
    if a == b:
        continue

    if a < b:
        need_point.append(b - a)
    else:
        has_margin.append((a - b, False))

has_margin = sorted(has_margin)
ans = len(need_point)
for x in need_point:
    while x > 0:
        y = has_margin[-1][0]
        if y >= x:
            has_margin[-1] = (y - x, True)
            x = 0
        else:
            has_margin.pop()
            x -= y
            ans += 1
if has_margin[-1][1]:
    ans += 1
print(ans)

