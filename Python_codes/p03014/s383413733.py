H, W = map(int, input().split())
G = [list(input()) for i in range(H)]


up = [[0] * W for i in range(H)]  # あるマスから上に連続していくつ障害物のないマスが続くか
right = [[0] * W for i in range(H)]  # あるマスから右に連続していくつ障害物のないマスが続くか
down = [[0] * W for i in range(H)]  # あるマスから下に連続していくつ障害物のないマスが続くか
left = [[0] * W for i in range(H)]  # あるマスから左に連続していくつ障害物のないマスが続くか


# up
for w in range(W):
    for h in range(1, H):
        if G[h - 1][w] == '#':
            continue
        up[h][w] = up[h - 1][w] + 1

# right
for h in range(H):
    for w in reversed(range(W - 1)):
        if G[h][w + 1] == '#':
            continue
        right[h][w] = right[h][w + 1] + 1

# down
for w in range(W):
    for h in reversed(range(H - 1)):
        if G[h + 1][w] == '#':
            continue
        down[h][w] = down[h + 1][w] + 1

# left
for h in range(H):
    for w in range(1, W):
        if G[h][w - 1] == '#':
            continue
        left[h][w] = left[h][w - 1] + 1


ans = 0
for h in range(H):
    for w in range(W):
        if G[h][w] == '#':
            continue
        ans = max(ans, up[h][w] + right[h][w] + down[h][w] + left[h][w] + 1)

print(ans)
