import sys
input = sys.stdin.readline

# dは隣接頂点間のコスト、Nは頂点の個数
def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    print(-1)
                    sys.exit()
                elif d[i][j] == d[i][k] + d[k][j] and k != i and k != j:
                    delete[i][j] = True
                    delete[j][i] = True                 
    return d

N = int(input())
inf = float("inf")
delete = [[False]*N for _ in range(N)]
# input

# d[i][v]:辺(i, v)間のコスト、存在しなければinf
d = [[int(x) for x in input().split()] for _ in range(N)]
d = warshall_floyd(d)

ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if delete[i][j]:
            continue
        ans += d[i][j]
print(ans)