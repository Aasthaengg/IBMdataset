H, W = map(int, input().split())

grid = []
for _ in range(H):
    line = input()
    # 後で都合が良いので末尾に足しておく
    line += "#"
    grid.append(line)

# 後で都合が良いので末尾に足しておく
grid.append("#" * W)
# print(grid)

G_h = []
for h in range(H):
    g = [-1] * W
    lamp_start = -1
    lamp = 0
    line = grid[h]
    for w in range(W):
        if line[w] == "#":
            g[w] = 0
        elif line[w] == ".":
            lamp += 1
            if lamp_start == -1:
                lamp_start = w
                # print("lampstart", w)
            if line[w + 1] == "#":
                # print("lampend", w)
                for i in range(lamp_start, w + 1):
                    g[i] = lamp
                lamp_start = -1
                lamp = 0
    G_h.append(g)

# print(G_h)

G_v = []
for w in range(W):
    g = [-1] * H
    lamp_start = -1
    lamp = 0
    line = []
    for hi in range(H):
        line.append(grid[hi][w])
    line.append("#")
    # line = grid[w]
    for h in range(H):
        if line[h] == "#":
            g[h] = 0
        elif line[h] == ".":
            lamp += 1
            if lamp_start == -1:
                lamp_start = h
                # print("lampstart", w)
            if line[h + 1] == "#":
                # print("lampend", w)
                for i in range(lamp_start, h + 1):
                    g[i] = lamp
                lamp_start = -1
                lamp = 0
    G_v.append(g)

# print(G_v)

ans = 0
for h in range(H):
    for w in range(W):
        tmp_ans = G_h[h][w] + G_v[w][h] - 1
        ans = max(ans, tmp_ans)
print(ans)
