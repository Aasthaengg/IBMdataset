H, W = map(int, input().split())

G = []
for _ in range(H):
    G.append(list(input()))

L, R, U, B = [], [], [], []
for y in range(H):
    targets = [L, R]
    ranges = [range(W), range(W-1, -1, -1)]
    for target, rng in zip(targets, ranges):
        row = [0] * W
        c = -1
        for x in rng:
            if G[y][x] == "#":
                c = -1
            else:
                c += 1
            row[x] = c
        target.append(row)
for x in range(W):
    targets = [U, B]
    ranges = [range(H), range(H-1, -1, -1)]
    for target, rng in zip(targets, ranges):
        col = [0] * H
        c = -1
        for y in rng:
            if G[y][x] == "#":
                c = -1
            else:
                c += 1
            col[y] = c
        target.append(col)

max_light = 0
for y in range(H):
    for x in range(W):
        light = L[y][x] + R[y][x] + U[x][y] + B[x][y] + 1
        max_light = max(light, max_light)
print(max_light)
