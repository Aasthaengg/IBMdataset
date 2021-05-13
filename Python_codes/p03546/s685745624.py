h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]
a = [list(map(int, input().split())) for _ in range(h)]

def warshall_floyd(d, n):
    # 経由する頂点
    for k in range(n):
        # 始点
        for i in range(n):
            # 終点
            for j in range(n):
                # 始点 - 終点よりも経由点を通った方が良いのであれば更新
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d
dist = warshall_floyd(c,10)
ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] == -1:
            continue
        ans += dist[a[i][j]][1]
print(ans)