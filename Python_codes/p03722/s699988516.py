def bellman_ford(n, edges, s, distance=None):
    if distance != None:
        d = distance[:]
    else :
        d = [float('inf')] * n
        d[s] = 0
    
    loop_cnt = 0
    while True:
        loop_cnt += 1
        update = False
        for i in range(len(edges)):
            e = edges[i]
            if d[e[0]] != float('inf') and d[e[1]] > d[e[0]] + e[2]:
                d[e[1]] = d[e[0]] + e[2]
                update = True

        if not update or loop_cnt > n: break
    return d

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a-1, b-1, -c))

dist = bellman_ford(n, edges, 0)
test = bellman_ford(n, edges, 0, dist)

if dist[n-1] != test[n-1]:
    print("inf")
else :
    print(-dist[n-1])