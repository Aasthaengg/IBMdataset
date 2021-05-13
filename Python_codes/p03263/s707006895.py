H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]
cnt = 0
done = [[0 for _ in range(W)] for _ in range(H)]
move = []

for i in range(H):
    for j in range(W):
        done[i][j] = 1
        if a[i][j] % 2 == 1:
            for i_d, j_d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (0 <= i + i_d < H and 0 <= j + j_d < W
                and done[i + i_d][j + j_d] == 0):
                    cnt += 1
                    move.append([i + 1, j + 1, i + i_d + 1, j + j_d + 1])
                    a[i + i_d][j + j_d] += 1
                    break

print(cnt)
for m in move:
    print(" ".join(map(str, m)))