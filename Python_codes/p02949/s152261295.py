n,m,p = map(int, input().split())
G = []
for i in range(m):
    a,b,c = map(int, input().split())
    G.append([a,b,c-p])

def bellmanFord(G, start_vertex):
    distance = [-float('inf') for i in range(n+1)]
    distance[start_vertex] = 0
    for i in range(2*n):
        for node,neighbor,cost in G:
            if distance[neighbor] < distance[node] + cost:
                if i < n:
                    distance[neighbor] = distance[node] + cost
                else:
                    distance[neighbor] = float('inf')
        if i == n-1:
            prev_ans = distance[n]
    if prev_ans != distance[n]:
        return -1
    else:
        return distance[n]

distance = bellmanFord(G, 1)
if distance == -1:
    ans = -1
else:
    ans = max(0, distance)
print(ans)
