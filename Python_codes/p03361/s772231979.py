H, W = map(int, input().split())

s = [list(input()) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(H):
    for j in range(W):
        can = False
        if s[i][j] == "#":
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x <= H - 1 and 0 <= y <= W - 1:
                    if s[x][y] == "#":
                        can = True
            if can is False:
                print("No")
                exit()

print("Yes")
