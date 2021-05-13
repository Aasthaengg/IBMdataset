H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
moves = ((1, 0), (0, 1), (0, -1), (-1, 0))
for y in range(H):
    for x in range(W):
        if s[y][x] == '#':
            flag = True
        else:
            continue
        for dy, dx in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if s[ny][nx] == '#':
                    flag = False
                    break
        if flag:
            print('No')
            exit()

print('Yes')