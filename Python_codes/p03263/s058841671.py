H,W = map(int, input().split())
a = [[int(i) for i in input().split()] for _ in range(H)]

move = []
for i in range(H):
    if i % 2 == 0:
        for j in range(W):
            if a[i][j] % 2 == 1:
                if j == W - 1 and i < H - 1:
                    move.append((i+1,j+1,i+2,j+1))
                    a[i][j] -= 1; a[i+1][j] += 1
                elif j < W - 1:
                    move.append((i+1,j+1,i+1,j+2))
                    a[i][j] -= 1; a[i][j+1] += 1
    else:
        for j in range(W-1, -1, -1):
            if a[i][j] % 2 == 1:
                if j == 0 and i < H - 1:
                    move.append((i+1,j+1,i+2,j+1))
                    a[i][j] -= 1; a[i+1][j] += 1
                elif j > 0:
                    move.append((i+1,j+1,i+1,j))
                    a[i][j] -= 1; a[i][j-1] += 1

print(len(move))
for ans in move:
    print(*ans, sep=" ")