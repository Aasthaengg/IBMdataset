h, w = map(int ,input().split())
s = [list(input()) for _ in range(h)]
check = [[0] * w for _ in range(h)]
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]
ans = 0

for i in range(h):
    for j in range(w):
        if check[i][j] == 1:
            continue
        black, white = 0, 0 

        stack = [[i, j]]
        check[i][j] = 1
        if s[i][j] == '#':
            black += 1
        else:
            white += 1

        while len(stack) > 0:
            x, y = stack.pop()
            tmp = s[x][y]
            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and tmp != s[nx][ny] and check[nx][ny] == 0:
                    stack.append([nx, ny])
                    check[nx][ny] = 1
                    if s[nx][ny] == '#':
                        black += 1
                    else:
                        white += 1

        ans += black * white

print(ans)

# %%
