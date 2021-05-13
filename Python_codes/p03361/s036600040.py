H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
dd = [[0, -1], [-1, 0], [0, 1], [1, 0]]
for i in range(H):
    for j in range(W):
        if s[i][j] == "#":
            for dx, dy in dd:
                nx = j + dx
                ny = i + dy
                if 0 <= nx < W and 0 <= ny < H:
                    if s[ny][nx] == "#":
                        break
            else:
                print("No")
                exit(0)

print("Yes")