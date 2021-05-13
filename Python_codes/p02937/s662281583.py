#!/usr/bin/env python3

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

s = input()
t = input()
flag = [False] * 26
for si in s:
    flag[ord(si) - ord('a')] = True
for ti in t:
    if not flag[ord(ti) - ord('a')]:
        print(-1)
        quit()
n = len(s)
S = s + s
idx = [[] for _ in range(26)]
for i in range(2*n):
    idx[ord(S[i]) - ord('a')].append(i)

dp = [[inf] * 26 for _ in range(n)]
for i in range(n):
    for j in range(26):
        if idx[j]:
            r = br(idx[j], i)
            dp[i][j] = idx[j][r]
c = ord(t[0]) - ord('a')
i = idx[c][0]
ans = i + 1
for ti in t[1:]:
    c = ord(ti) - ord('a')
    ni = dp[i][c] % n
    ans += dp[i][c] - i
    i = ni
print(ans)