N,M = map(int, input().split())
g = {}
for v in range(1,N*3+1):
    g[v] = []

for _ in range(M):
    u,v = map(int, input().split())
    g[u + N*0].append(v + N*1)
    g[u + N*1].append(v + N*2)
    g[u + N*2].append(v + N*0)

S,T = map(int, input().split())

visiting = [S]
visited = {S:0}
while visiting:
    v = visiting.pop(0)
    if v == T:
        break

    for v2 in g[v]:
        if v2 not in visited:
            visiting.append(v2)
            visited[v2] = visited[v]+1

if T in visited:
    print(visited[T] // 3)
else:
    print(-1)
