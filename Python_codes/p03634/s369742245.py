from heapq import heappush, heappop

def dijkstra(s):
    '''
    始点sから各頂点への最短距離を求める
    '''
    d = [float("inf")] * n
    d[s] = 0
    used = [False] * n
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


n = int(input())

edge = [[] for _ in range(n)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    edge[a-1].append([c, b-1])
    edge[b-1].append([c, a-1])

q, k = map(int, input().split())

dist = dijkstra(k-1)

res = [0] * q
for i in range(q):
    x, y = map(int, input().split())
    res[i] = dist[x-1] + dist[y-1]

for v in res:
    print(v)