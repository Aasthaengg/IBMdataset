H, W = map(int, input().split())
G = []
for i in range(H):
    G.append(list(input()))
fd = [[-1, 0], [1, 0], [0, 1], [0, -1]]
for i in range(H-1):
    for j in range(W-1):
        if G[i][j] == '#':
            boo = False
            for x, y in fd:
                if i+y < 0 or i+y >= H or j+x < 0 or j+y >= W:
                    continue
                if G[i+y][j+x] == '#':
                    boo = True
            if not boo:
                print('No')
                exit()
print('Yes')