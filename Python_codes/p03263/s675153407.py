#!/usr/bin/env python3
#C

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

h, w = LI()
a = [LI() for _ in range(h)]

ans = []
dx, dy = [1, 0], [0, 1]
for i in range(h):
    for j in range(w):
        if a[i][j] % 2:
            for k in range(2):
                ny, nx = i + dy[k], j + dx[k]
                if 0 <= ny < h and 0 <= nx < w:
                    if a[ny][nx] % 2:
                        a[ny][nx] += 1
                        a[i][j] -= 1
                        ans.append((i, j, ny, nx))
                        break
            else:
                if j + 1 < w:
                    a[i][j+1] += 1
                    a[i][j] -= 1
                    ans.append((i, j, i, j+1))
                elif i + 1 < h:
                    a[i+1][j] += 1
                    a[i][j] -= 1
                    ans.append((i, j, i+1, j))

print(len(ans))
for (i, j, k, l) in ans:
    print(i+1, j+1, k+1, l+1) 