import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
D, G = map(int, input().split())

P = [0] * D
C = [0] * D
for i in range(D):
    P[i], C[i] = map(int, input().split())


ans = INF
for i in range(1 << D):
    points = 0
    solved = 0
    for j in range(D):
        if i & 1 << j > 0:
            points += C[j]
            points += P[j] * (j + 1) * 100
            solved += P[j]

    left = G - points
    for j in range(D - 1, -1, -1):
        if left <= 0:
            break
        if i & 1 << j > 0:
            continue
        val = min(100 * (j + 1) * (P[j] - 1), left)
        left -= val
        if val % (100 * (j + 1)) != 0:
            solved += val // (100 * (j + 1)) + 1
        else:
            solved += val // (100 * (j + 1))

    if left > 0:
        continue
    ans = min(ans, solved)
print(ans)

            

