from heapq import heappush, heappop


def dijkstra(s):
    '''
    始点sから各頂点への最短距離を求める
    '''
    d = [float("inf")] * 10
    d[s] = 0
    used = [False] * 10
    used[s] = True
    edgelist = []

    for e in edge[s]:
        heappush(edgelist, e)

    while edgelist:
        cost, v = heappop(edgelist)
        if used[v]:
            continue
        d[v] = cost
        used[v] = True
        for e in edge[v]:
            if not used[e[1]]:
                heappush(edgelist, [e[0] + d[v], e[1]])

    return d


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

edge = [[] for _ in range(10)]
for i in range(10):
    for j in range(10):
        edge[i].append([c[i][j], j])
        edge[j].append([c[j][i], i]) 

dist = []
for i in range(10):
    dist.append(dijkstra(i))

res = 0
for i in range(h):
    for j in range(w):
        if a[i][j] >= 0:
            res += dist[a[i][j]][1]

print(res)