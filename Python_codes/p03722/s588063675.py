def bell(edges, n):
    count = 0
    dist = [float('inf') for i in range(n)]
    dist[0] = 0

 
    for i in range(n):
        for edge in edges:
            if dist[edge[1]] > dist[edge[0]] + edge[2] and edge[0] != float('inf'):
                dist[edge[1]] = dist[edge[0]] + edge[2]
                if (i == n - 1) & (edge[1] == n - 1):
                    print('inf')
                    exit()
                
    return dist
 
 
n,m = map(int,input().split())
edges = []
for _ in range(m):
    a, b, c = (int(x) for x in input().split())
    edges.append([a-1, b-1, -c])
 
res = bell(edges, n)
 
print(-res[n-1])