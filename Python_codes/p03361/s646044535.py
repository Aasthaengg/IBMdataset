H, W = map(int, input().split())
s = [input() for h in range(H)]

for h in range(H):
    for w in range(W):
        if s[h][w] == '#':
            flag = False
            for dx, dy in ([-1, 0], [0, -1], [1, 0], [0, 1]):
                x = h + dx
                y = w + dy
                if x<0 or x>=H:
                    continue
                if y<0 or y>=W:
                    continue
                if s[x][y] == '#':
                    flag = True
                    break
            if not flag:
                print('No')
                exit()

print('Yes')