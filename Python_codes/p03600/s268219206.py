N = int(input())
dist = [[float("inf") if i != j else 0 for i in range(N)] for j in range(N)]

for i in range(N):
    dist[i] = list(map(int, input().split()))

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                exit()

for i in range(N):
    for j in range(i + 1, N):
        for k in range(N):
            if k == i or k == j:
                continue
            # kを通る迂回ルートが存在する場合dist[i][j]取り除く(=カウントしない)
            if dist[i][j] == dist[i][k] + dist[k][j]:
                break
        else:
            # 迂回ルートが一つもなかった場合は答えに加算する
            ans += dist[i][j]
print(ans)