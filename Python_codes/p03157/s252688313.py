H, W = map(int, input().split())
S = [input() for _ in range(H)]

G = [[None for j in range(W)] for i in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

for i in range(H):
    for j in range(W):
        if G[i][j] is not None:
            continue
        if S[i][j] == '#':
            color = 1
        else:
            color = 0
        stack = [(i, j, color)]
        G[i][j] = count
        while stack:
            x, y, c = stack.pop()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if not (0 <= nx < H and 0 <= ny < W):
                    continue
                if G[nx][ny] is not None:
                    continue
                if S[nx][ny] == '#':
                    nc = 1
                else:
                    nc = 0
                if nc == c:
                    continue
                G[nx][ny] = count
                stack.append((nx, ny, nc))
        count += 1

C = [[0, 0] for _ in range(count)]

for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            C[G[i][j]][0] += 1
        else:
            C[G[i][j]][1] += 1

res = 0

for b, w in C:
    res += b * w

print(res)