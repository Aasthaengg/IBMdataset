N,M = map(int, input().split())
L = [[int(u) for u in input().split()] for i in range(M)]
S,T = map(int, input().split())

edge = [[] for i in range(N+1)]
for i in range(M):
    edge[L[i][0]].append(L[i][1])
    
q = [S]
INF = 10**9
visited = [[INF+1, INF+1, INF+1] for i in range(N+1)]
visited[S][0] = 0
cnt = 1
while len(q) > 0:
    length = len(q)
    for j in range(length):
        temp = q.pop(0)
        for i in range(len(edge[temp])):
            if visited[edge[temp][i]][cnt%3] > INF:
                q.append(edge[temp][i])
                visited[edge[temp][i]][cnt%3] = cnt
    cnt += 1
    
if visited[T][0] < INF:
    print(visited[T][0]//3)
else:
    print(-1)