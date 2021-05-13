H, W = map(int, input().split())

G = []
for _ in range(H):
    g = []
    line = input()
    for i in range(W):
        g.append(line[i])
    G.append(g)

# 左に何マス行けるか
G_left = [[0] * W for _ in range(H)]
for h in range(H):
    cnt = 0
    for w in range(W):
        if G[h][w] == "#":
            cnt = 0
            G_left[h][w] = 0
        elif G[h][w] == ".":
            cnt += 1
            G_left[h][w] = cnt
# print(G_left)

# 右に何マス行けるか
G_right = [[0] * W for _ in range(H)]
for h in range(H):
    cnt = 0
    for w in range(W - 1, -1, -1):
        if G[h][w] == "#":
            cnt = 0
            G_right[h][w] = 0
        elif G[h][w] == ".":
            cnt += 1
            G_right[h][w] = cnt
# print(G_right)

# 上に何マス行けるか
G_up = [[0] * W for _ in range(H)]
for w in range(W):
    cnt = 0
    for h in range(H):
        if G[h][w] == "#":
            cnt = 0
            G_up[h][w] = 0
        elif G[h][w] == ".":
            cnt += 1
            G_up[h][w] = cnt
# print(G_up)

# 下に何マス行けるか
G_down = [[0] * W for _ in range(H)]
for w in range(W):
    cnt = 0
    for h in range(H - 1, -1, -1):
        if G[h][w] == "#":
            cnt = 0
            G_down[h][w] = 0
        elif G[h][w] == ".":
            cnt += 1
            G_down[h][w] = cnt
# print(G_down)
ans = 0
for h in range(H):
    for w in range(W):
        tmp = G_left[h][w] + G_right[h][w] + G_up[h][w] + G_down[h][w] - 3
        ans = max(ans, tmp)

print(ans)
