from collections import deque
import sys
sys.setrecursionlimit(10 ** 9)

N, M, P = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

to = [[] for _ in range(N + 1)]
ot = [[] for _ in range(N + 1)]
edges = [[] for _ in range(N + 1)]

for a, b, c in X:
    edges[a].append((b, c - P))
    to[a].append(b)
    ot[b].append(a)

ok_1 = [False] * (N + 1)
ok_n = [False] * (N + 1)

def dfs_1(u):
    if ok_1[u]:
        return
    
    ok_1[u] = True
    for v in to[u]:
        dfs_1(v)
        
def dfs_n(u):
    if ok_n[u]:
        return
    
    ok_n[u] = True
    for v in ot[u]:
        dfs_n(v)

dfs_1(1)
dfs_n(N)

INF = 10 ** 9 + 7
d = [INF] * (N + 1)
d[1] = 0
updated = True
cnt = 0
while updated and cnt <= N:
    updated = False
    cnt += 1
    for u in range(1, N + 1):
        if not ok_1[u] or not ok_n[u]:
            continue
            
        for v, c in edges[u]:
            if not ok_1[v] or not ok_n[v]:
                continue
                
            if d[v] > d[u] - c:
                d[v] = d[u] - c
                updated = True

if cnt > N:
    print(-1)
else:
    print(max(0, -d[-1]))
