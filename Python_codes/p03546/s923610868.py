H,W = map(int,input().split())
C = [list(map(int,input().split())) for _ in range(10)]
A = [list(map(int,input().split())) for _ in range(H)]
dist = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    for j in range(10):
        dist[i][j] = C[i][j]
for k in range(10):
    for i in range(10):
        for j in range(10):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])
cnt = 0
for i in range(H):
    for j in range(W):
        if A[i][j]>=0:
            cnt += dist[A[i][j]][1]
print(cnt)