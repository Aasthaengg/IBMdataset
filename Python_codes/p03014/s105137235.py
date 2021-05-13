H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

cnt = [[0 for i in range(W)] for j in range(H)]

# 横
for i in range(H):
    done = [0] * W
    for j in range(W):
        if done[j]:
            continue
        if maze[i][j] == "#":
            continue
        l = 0
        while j + l < W:
            if maze[i][j+l] == "#":
                break
            l += 1
        for k in range(j,j+l):
            done[k] = 1
            cnt[i][k] += l





# 縦
for i in range(W):
    done = [0] * H
    for j in range(H):
        if done[j]:
            continue
        if maze[j][i] == "#":
            continue
        l = 0
        while j + l < H:
            if maze[j+l][i] == "#":
                break
            l += 1
        for k in range(j,j+l):
            done[k] = 1
            cnt[k][i] += l

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, cnt[i][j]-1)
print(ans)