import sys
sys.setrecursionlimit(10 ** 9)

N, M, P = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(M)]

edges = [[] for _ in range(N)]
to = [[] for _ in range(N)]
ot = [[] for _ in range(N)]

for a, b, c in X:
    a -= 1
    b -= 1
    c = -(c - P)
    edges[a].append((b, c))
    to[a].append(b)
    ot[b].append(a)

ok_1 = [False] * N
ok_n = [False] * N

# Reachable
def dfs(u):
    if ok_1[u]:
        return
    
    ok_1[u] = True
    for v in to[u]:
        dfs(v)
        
def rdfs(u):
    if ok_n[u]:
        return
    
    ok_n[u] = True
    for v in ot[u]:
        rdfs(v)
        
dfs(0)
rdfs(N - 1)
flag = [ok_1[i] & ok_n[i] for i in range(N)]

# Bellman ford
INF = 10 ** 9 + 7
d = [INF] * N
d[0] = 0
cnt = 0
updated = True
while updated and cnt <= N:
    updated = False
    cnt += 1
    for u in range(N):
        if not flag[u]:
            continue
        for v, c in edges[u]:
            if not flag[v]:
                continue

            value = d[u] + c
            if d[v] > d[u] + c:
                d[v] = value
                updated = True

if cnt > N:
    print(-1)
else:
    print(max(0, -d[-1]))
