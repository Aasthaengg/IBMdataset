n, m = map(lambda x: int(x), input().split())
a = [0] * m
b = [0] * m
c = [0] * m
for i in range(m):
    a[i], b[i], c[i] = map(lambda x: int(x), input().split())

def dijkstra(graph, start, end):
    cost = [1000*100 for _ in range(n+1)]
    fixed = [False for _ in range(n+1)]
    cost[start] = 0
    fixed[start] = True
    tmp_sta = start
    while True:
        tmp_min = 1000*100
        for i in graph[tmp_sta]:
            cost[i[0]] = min(cost[i[0]], cost[tmp_sta]+i[1])
        for i in range(1, n+1):
            if tmp_min > cost[i] and fixed[i] == False:
                tmp_min = cost[i]
                tmp_sta = i
        if tmp_sta == end:
            return tmp_min
        else:
            fixed[tmp_sta] = True
    
graph = {}
for i in range(1, n+1):
    graph[i] = []
for i in range(m):
    graph[a[i]].append((b[i], c[i]))
    graph[b[i]].append((a[i], c[i]))
    
ans = 0
for i in range(m):
    if c[i] > dijkstra(graph, a[i], b[i]):
        ans += 1
print(ans)