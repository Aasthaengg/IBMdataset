N, M = map(int, input().split())
edges = []
G = [[10**8]*N for _ in range(N)]   # 1-indexed
for _ in range(M):
    A, B, C = map(int, input().split())
    # 無向グラフ
    G[A-1][B-1] = C
    G[B-1][A-1] = C
    edges.append((A-1, B-1, C))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                G[i][j] = 0
            if G[i][j] > G[i][k]+G[j][k]:
                G[i][j] = G[i][k]+G[j][k]

ans = 0
for A, B, C in edges:
    flg = False
    for i in range(N):
        for j in range(N):
            if G[i][A]+C+G[B][j] == G[i][j]:
                flg = True
    if flg is False:
        ans += 1
print(ans)
