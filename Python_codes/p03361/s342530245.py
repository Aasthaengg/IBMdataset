H, W = map(int, input().split())
Map = [[s for s in input()] for _ in range(H)]

for i in range(H):
    for j in range(W):
        if Map[i][j] == '#':
            for dy, dx in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                ny = i + dy
                nx = j + dx
                if ny < 0 or ny >= H or nx < 0 or nx >= W:
                    continue
                if Map[ny][nx] == '#':
                    break
            else:
                print('No')
                exit()
print('Yes')