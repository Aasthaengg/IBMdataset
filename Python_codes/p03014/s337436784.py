H, W = map(int, input().split())

grid = []

for i in range(H):
    s = input()
    r = []
    for j, x in enumerate(s):
        r.append(x)

    grid.append(r)


H_cnt = [[0] * W for _ in range(H)]
W_cnt = [[0] * W for _ in range(H)]

for r in range(H):
    idx = 0

    while idx < W:
        if grid[r][idx] == '.' and (idx == 0 or grid[r][idx - 1] == '#'):
            cnt = 1
            st = idx
            if idx == W - 1 or grid[r][idx + 1] == '#':
                W_cnt[r][idx] = 1
        elif grid[r][idx] == '.' and (idx == W - 1 or grid[r][idx + 1] == '#'):
            cnt += 1
            for i in range(st, idx + 1):
                W_cnt[r][i] = cnt
        elif grid[r][idx] == '.':
            cnt += 1
        elif grid[r][idx] == '#':
            pass

        idx += 1

for c in range(W):
    idx = 0

    while idx < H:
        if grid[idx][c] == '.' and (idx == 0 or grid[idx - 1][c] == '#'):
            cnt = 1
            st = idx
            if idx == H - 1 or grid[idx + 1][c] == '#':
                H_cnt[idx][c] = 1
        elif grid[idx][c] == '.' and (idx == H - 1 or grid[idx + 1][c] == '#'):
            cnt += 1
            for i in range(st, idx + 1):
                H_cnt[i][c] = cnt
        elif grid[idx][c] == '.':
            cnt += 1
        elif grid[idx][c] == '#':
            pass

        idx += 1

max_ = 0
for r in range(H):
    for c in range(W):
        max_ = max(max_, W_cnt[r][c] + H_cnt[r][c] - 1)

print(max_)
