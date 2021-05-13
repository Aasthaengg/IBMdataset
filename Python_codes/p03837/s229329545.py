N, M = map(int, input().split())
path = [[float("inf")]*N for i in range(N)]
ans = [[[float("inf")]]*N for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    path[a-1][b-1] = c
    path[b-1][a-1] = c
    ans[a-1][b-1] = [i]
    ans[b-1][a-1] = [i]
for i in range(N):
    path[i][i] = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if path[i][k]+path[k][j] < path[i][j]:
                path[i][j] = path[i][k]+path[k][j]
                ans[i][j] = ans[i][k]+ans[k][j]
total = set()
for i in range(N):
    for j in range(N):
        p = set(ans[i][j])
        total = total|p
print(M-len(set(total))+1)
        
