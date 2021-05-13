h, w = map(int, input().split())
G = [list(input()) for _ in range(h)]
flg = True
for i in range(h):
    for j in range(w):
        if G[i][j] == "#":
            count = 1
            for u, v in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                y, x = i + u, j + v
                if 0 <= x < w and 0 <= y < h:
                    # print(i, j, G[y][x])
                    if G[y][x] == "#":
                        count += 1
            if count < 2:
                flg = False
                break
    if not flg:
        break

print("Yes" if flg else "No")