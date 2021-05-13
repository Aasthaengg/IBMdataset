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

N = int(input())
S = input()

es = [0] * (N + 1)
ws = [0] * (N + 1)

for i, c in enumerate(S):
    if c == 'E':
        es[i + 1] = es[i] + 1
        ws[i + 1] = ws[i]
    elif c == 'W':
        ws[i + 1] = ws[i] + 1
        es[i + 1] = es[i]
    
ans = INF
for i in range(N):
    cnt = ws[i] + (es[N] - es[i + 1])
    ans = min(ans, cnt)
print(ans)
