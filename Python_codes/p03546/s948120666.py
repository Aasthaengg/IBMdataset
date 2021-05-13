h, w = map(int, input().split())
G = []
ans = 0
for i in range(10):
    G.append(list(map(int, input().split())))
for i in range(10):
    G[i][i] = 0
for k in range(10):
    for i in range(10):
        for j in range(10):
            G[i][j] = min(G[i][j], G[i][k] + G[k][j])
for i in range(h):
    wall = list(map(int, input().split()))
    for j in range(w):
        if wall[j] == -1:
            continue
        ans += G[wall[j]][1]
print(ans)


