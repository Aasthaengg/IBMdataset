N, M = map(int, input().split())
abc = [[int(x) for x in input().split()] for _ in range(M)]
Edges = [None]*M
for i in range(M):
    Edges[i] = (abc[i][0]-1, abc[i][1]-1, -abc[i][2])
def bellman_ford(N, edges, s):
    dist = [float("inf")]*(N)
    dist[s] = 0
    for n in range(N):
        for (u,v,c) in edges:
            if dist[u] != float("inf") and dist[v] >  dist[u] + c:
                dist[v] = dist[u] + c
                if n == N-1 and v == N-1:
                    return "inf"
    return -dist[-1]
print(bellman_ford(N, Edges, 0))

