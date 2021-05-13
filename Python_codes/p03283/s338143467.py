N, M, Q = map(int,input().split())
graph = [[0 for i in range(N+1)] for j in range(N+1)]
for _ in range(M):
    L, R = map(int,input().split())
    graph[L-1][R] += 1

for i in range(N-1,-1,-1):
    for j in range(1,N+1):
        graph[i][j] += graph[i+1][j] + graph[i][j-1] - graph[i+1][j-1]

for _ in range(Q):
    p, q = map(int,input().split())
    print(graph[p-1][q])