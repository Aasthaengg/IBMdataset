from itertools import product

H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y, x in product(range(H), range(W)):
    if S[y][x] == "#":
        continue

    count = 0
    for i, j in product((-1, 0, 1), repeat=2):
        if not (0 <= y + i < H and 0 <= x + j < W):
            continue
        if S[y + i][x + j] == "#":
            count += 1
    S[y][x] = str(count)

print("\n".join("".join(r) for r in S))