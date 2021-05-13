def warshall_floyd():
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])

N, M = map(int, input().split())
d = [[10**18]*N for _ in range(N)]

for i in range(N):
    d[i][i] = 0
    
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    d[a-1][b-1] = c
    d[b-1][a-1] = c
    edges.append((a-1, b-1, c))

warshall_floyd()
ans = 0

for a, b, c in edges:
    flag = True
    
    for i in range(N):
        for j in range(N):
            if d[i][a]+c+d[b][j]==d[i][j]:
                flag = False
    
    if flag:
        ans += 1

print(ans)