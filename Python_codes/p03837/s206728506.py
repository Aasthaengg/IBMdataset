import sys
input = sys.stdin.readline

# dは隣接頂点間のコスト、Nは頂点の個数
def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

# input
N, W = [int(x) for x in input().split()] # N:頂点数、W:辺の数
inf = float("inf")

# d[i][v]:辺(i, v)間のコスト、存在しなければinf
d = [[inf] * N for _ in range(N)]
abc = []

for _ in range(W):
    a, b, c = [int(x) for x in input().split()]
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
    abc.append([a, b, c])

# 自身の頂点へのコストは0
for i in range(N):
    d[i][i] = 0

d = warshall_floyd(d)
cnt = 0

for i in range(W):
    a, b, c = abc[i]
    if d[a - 1][b - 1] != c:
        cnt += 1

print(cnt)

