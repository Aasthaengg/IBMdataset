from collections import defaultdict as dd

N,M = map(int,input().split())
check = dd(int)
edge = []
res = 0
dist = [[10**18]*N for _ in range(N)]
for i in range(M):
    p,q,c = map(int,input().split())
    dist[p-1][q-1] = c
    dist[q-1][p-1] = c
    edge.append((p-1,q-1,c))
    check[(max(p-1,q-1),min(p-1,q-1))] = 1
for i in range(N):
    dist[i][i] = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            if dist[j][k] > dist[j][i]+dist[i][k]:
                dist[j][k] = dist[j][i] + dist[i][k]

for now in edge:
    for s in range(N):
        for t in range(N):
            if dist[s][t] == dist[s][now[0]] + now[2] + dist[now[1]][t]:
                check[(max(now[0],now[1]),min(now[0],now[1]))] = 0
for v in check.items():
    res += v[1]
    #print(v[0])
print(res)