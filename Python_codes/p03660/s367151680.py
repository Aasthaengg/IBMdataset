#coding: utf-8
import math
import heapq
import bisect
import numpy as np
from collections import Counter, deque
#from scipy.misc import comb

N = int(input())
G = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

d_F = [0] + [-1]*(N-1)
d_S = [-1]*(N-1) + [0]

q_F = deque([0])
q_S = deque([N-1])

while len(q_F) > 0:
    u = q_F.popleft()
    for v in G[u]:
        if d_F[v] == -1:
            d_F[v] = d_F[u] + 1
            q_F.append(v)

while len(q_S) > 0:
    u = q_S.popleft()
    for v in G[u]:
        if d_S[v] == -1:
            d_S[v] = d_S[u] + 1
            q_S.append(v)

black = 0
white = 0
for i in range(N):
    if d_F[i] <= d_S[i]: black += 1
    else: white += 1

if black > white:
    print("Fennec")
else:
    print("Snuke")