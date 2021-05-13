INF = 10**18

N,M = map(int,input().split())
edge = [list(map(int,input().split())) for _ in range(M)]
graph = [[INF for j in range(N)] for i in range(N)]

for i in range(N):
    graph[i][i] = 0

for e in edge:
    graph[e[0]-1][e[1]-1] = e[2]
    graph[e[1]-1][e[0]-1] = e[2]
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] != INF and graph[k][j] != INF:
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

ans = 0

for e in edge:
    if graph[e[0]-1][e[1]-1] != e[2]:
        ans += 1
        
print(ans)