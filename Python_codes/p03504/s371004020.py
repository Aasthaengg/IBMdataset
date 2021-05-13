# -*- coding: utf-8 -*-
import sys
from heapq import heappop,heappush
from collections import deque
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N,C = map(int,readline().split())
data = [[] for _ in range(C+1)]
for i in range(N):
    s,t,c = map(int,readline().split())
    data[c].append((s,t))

TV = []
for d in data:
    N = len(d)
    if N == 0:
        continue
    d = sorted(d)
    g = d[0][1]
    cnt = 0
    for i in range(N-1):
        if g == d[i+1][0]:
            cnt += 1
        else:
            TV.append((d[i-cnt][0],d[i][1]))
            cnt = 0
        g = d[i+1][1]
    TV.append((d[-(1+cnt)][0],d[-1][1]))

TV = sorted(TV)
len_TV = len(TV)
q = [TV[0][1]]

for i in range(1,len_TV):
    s = TV[i][0]
    g = TV[i][1]
    m = heappop(q)
    if m >= s:
        heappush(q,m)
    heappush(q,g)

print(len(q))