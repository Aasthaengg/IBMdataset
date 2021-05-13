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

A, B, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = INF
for i in range(M):
    x, y, c = map(int, input().split())
    x -= 1
    y -= 1
    now = A[x] + B[y] - c
    ans = min(now, ans)
min_a = min(A)
min_b = min(B)
ans = min(ans, min_a + min_b)
print(ans)