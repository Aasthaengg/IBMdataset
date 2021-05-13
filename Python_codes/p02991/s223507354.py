n,m = map(int,input().split())
if m==0:
    print(-1)
    exit()
es = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    es[u].append(v)
s,t = map(int,input().split())

INF = 10**9
dist = [[INF,INF,INF] for _ in range(n+1)]

d = 0
q = [s]

while q:
    d += 1
    r = d%3
    qq = []
    for u in q:
        for v in es[u]:
            if dist[v][r] == INF:
                dist[v][r] = d
                qq.append(v)
    q = qq

d = dist[t][0]
print(-1 if d==INF else d//3)