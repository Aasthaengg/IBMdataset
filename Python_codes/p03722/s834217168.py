import sys
input = sys.stdin.readline
from collections import defaultdict
N,M = map(int,input().split())
abc = [list(map(int,input().split())) for i in range(M)]

g = defaultdict(list)
rg = defaultdict(list)
for a,b,c in abc:
    g[a].append((b,c))
    rg[b].append(a)

inf = 10**20
score = [-inf]*(N+1)
score[1] = 0

for i in range(N-1):
    for v in range(1,N+1):
        for nv, c in g[v]:
            if score[v] + c > score[nv]:
                score[nv] = score[v] + c

update = [False]*(N+1)
for v in range(1,N+1):
    for nv, c in g[v]:
        if score[v] + c > score[nv]:
            score[nv] = score[v] + c
            update[v] = True

visited = [False]*(N+1)
l = [N]
while l:
    v = l.pop()
    visited[v] = True
    for nv in rg[v]:
        if not visited[nv]:
            l.append(nv)
for u,v in zip(update, visited):
    if u and v:
        print('inf')
        exit()

print(score[N])
