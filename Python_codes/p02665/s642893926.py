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

cons = []
cur = 0
mn, mx = 0, 0
for i in range(N, -1, -1):
    mn = ((mn + 1) // 2) + A[i]
    mx = mx + A[i]
    if mn > 2 ** i:
        print(-1)
        exit()
    cons.append((mn, mx))
cons = list(reversed(cons))
ans = 0
cnt_node = 1
for i in range(N + 1):
    mn, mx = cons[i]
    now = min(mx, cnt_node)
    ans += now
    cnt_node = (now - A[i]) * 2
print(ans)

