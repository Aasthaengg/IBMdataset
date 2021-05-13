H, W = map(int, input().split())
dist = [list(map(int, input().split())) for _ in range(10)]
for i in range(10):
    for j in range(10):
        for k in range(10):
            dist[j][k] = min(dist[j][k], dist[j][i] + dist[i][k])
ans = 0
for _ in range(H):
    for i in list(map(int, input().split())):
        if i == 1 or i == -1:
            continue
        ans += dist[i][1]
print(ans)