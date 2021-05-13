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
H, W, K = map(int, input().split())
S = [input() for _ in range(H)]
acc = [[0] * (W + 1) for _ in range(H)]
for i in range(H):
    for j in range(1, W + 1):
        acc[i][j] = acc[i][j - 1] + int(S[i][j - 1])


ans = INF
for bit in range(1 << (H - 1)):
    base = 0
    vertical = []
    for i in range(H - 1):
        if bit & 1 << i > 0:
            vertical.append((base, i))
            base = i + 1
    vertical.append((base, H - 1))

    tmp_ans = len(vertical) - 1
    prev = 0
    j = 1
    valid = False
    while j <= W:
        ok = True
        for v in vertical:
            now = 0
            for i in range(v[0], v[1] + 1):
                now += acc[i][j] - acc[i][prev]
            if now > K:
                ok = False
        if ok:
            valid = True
        else:
            if valid:
                prev = j - 1
                tmp_ans += 1
                valid = False
                continue
            else:
                break
        j += 1
    if valid:
        ans = min(tmp_ans, ans)
print(ans)