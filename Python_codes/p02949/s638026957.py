import sys
sys.setrecursionlimit(10**9)

N,M,P = map(int,input().split())
edges = []
L = [[] for i in range(N)]
utov = [[] for i in range(N)]
vtou = [[] for i in range(N)]

for i in range(M) :
    u,v,cost = map(int,input().split())
    u -= 1
    v -= 1
    cost -= P
    cost *= -1
    edges.append([u,v,cost])
    utov[u].append(v)
    vtou[v].append(u)

reachableFromS = [False]*N
reachableFromG = [False]*N

def dfs(u) :
    if reachableFromS[u] :
        return
    reachableFromS[u] = True
    for v in utov[u] :
        dfs(v)

def dfs2(v) :
    if reachableFromG[v] :
        return
    reachableFromG[v] = True
    for u in vtou[v] :
        dfs2(u)

dfs(0)
dfs2(N-1)

OK = [reachableFromS[i] * reachableFromG[i] for i in range(N)]

dist = [float("inf")]*N
dist[0] = 0

ans = 0
step = 0
update = True

while update :
    update = False
    for i in range(M) :
        u,v,cost = edges[i]
        if OK[u] * OK[v] == 0 :
            continue
        if dist[v] > dist[u] + cost :
            dist[v] = dist[u] + cost
            update = True
    
    step += 1
    if step > N :
        ans = -1
        break

if ans != -1 :
    ans = max(0, dist[N-1] * (-1))
print(ans)
