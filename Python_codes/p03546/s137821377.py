def floyd_warshall(dist):
    v = len(dist)
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

h,w = map(int,input().split())
c = [list(map(int,input().split())) for _ in range(10)]
floyd_warshall(c)
A = [list(map(int,input().split())) for _ in range(h)]
ans = 0
for i in range(h):
    for j in range(w):
        if A[i][j] != -1:
            ans += c[A[i][j]][1]
print(ans)