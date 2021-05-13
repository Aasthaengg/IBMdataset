H, W = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
A = [list(map(int, input().split())) for _ in range(H)]

def warshall_floyd(d):
    #d[i][j]: iからjへの最短距離
    for k in range(10):
        for i in range(10):
            for j in range(10):
                d[i][j] = min(d[i][j],d[i][k] + d[k][j])
    return d

d = warshall_floyd(c)
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1 and A[i][j] != 1:
            ans += d[A[i][j]][1]
print(ans)