from copy import deepcopy

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

graph = deepcopy(A)
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans = 0
for u in range(N):
    if ans < 0:
        break
    for v in range(N):
        if graph[u][v] < A[u][v]:
            ans = -1
            break
            
        flg = True
        for w in range(N):
            if w == u or w == v:
                continue
            flg &= graph[u][v] < graph[u][w] + graph[w][v]
        
        if flg:
            ans += graph[u][v]

print(ans // 2)

