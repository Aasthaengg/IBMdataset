import sys
input = sys.stdin.readline
N,M = map(int,input().split())
XY = [tuple(map(int,input().split())) for i in range(M)]

es = [[] for _ in range(N)]
indeg = [0] * N
for x,y in XY:
    x,y = x-1,y-1
    es[x].append(y)
    indeg[y] += 1

from collections import deque
q = deque()
for i in range(N):
    if indeg[i] == 0:
        q.append(i)

dp = [0] * N
while q:
    v = q.popleft()
    for to in es[v]:
        indeg[to] -= 1
        if indeg[to] == 0: q.append(to)
        dp[to] = max(dp[to], dp[v] + 1)

print(max(dp))