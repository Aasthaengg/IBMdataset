def bellman_ford(s):
    '''
    始点sから各頂点への最短距離を求める (重み付き有向グラフ)
    '''
    dist = [float('inf')] * v
    dist[s] = 0
    neg = [False] * v

    for i in range(v-1):
        for p, q, cost in edge:
            if dist[p] != float('inf') and dist[q] > dist[p] + cost:
                dist[q] = dist[p] + cost
    
    for i in range(v):
        for p, q, cost in edge:
            if dist[p] != float('inf') and dist[q] > dist[p] + cost:
                dist[q] = dist[p] + cost
                neg[q] = True
            if neg[p]:
                neg[q] = True

    if neg[v-1]:
        return False
    else:
        return -dist[v-1]


v, e = map(int, input().split())

edge = []
for _ in range(e):
    s, t, d = map(int, input().split())
    edge.append([s-1, t-1, -d])

res = bellman_ford(0)

if not res:
    print('inf')
else:
    print(res)