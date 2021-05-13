H, W = map(int, input().split())
field = [list(input()) for _ in range(H)]

div = 10**9+7

patterns = [[0 for _ in range(W)] for __ in range(H)]
patterns[0][0] = 1


for y in range(H):
    for x in range(W):
        if x + 1 < W and field[y][x+1] != '#':
            patterns[y][x+1] += patterns[y][x] % div
        if y + 1 < H and field[y+1][x] != '#':
            patterns[y+1][x] += patterns[y][x] % div

print(patterns[-1][-1] % div)