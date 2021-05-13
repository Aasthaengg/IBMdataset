h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

row_list = [[0] * w for _ in range(h)]
for i in range(h):
    r = 0
    cnt = 0
    for l in range(w):
        if s[i][l] == '#':
            row_list[i][l] = 0
            r += 1
            cnt = 0
            continue

        while r < w and s[i][r] == '.':
            cnt += 1
            r += 1

        row_list[i][l] = cnt

col_list = [[0] * h for _ in range(w)]
for i in range(w):
    r = 0
    cnt = 0
    for l in range(h):
        if s[l][i] == '#':
            col_list[i][l] = 0
            r += 1
            cnt = 0
            continue

        while r < h and s[r][i] == '.':
            cnt += 1
            r += 1

        col_list[i][l] = cnt

res = 0
for i in range(h):
    for j in range(w):
        res = max(res, row_list[i][j] + col_list[j][i] - 1)

print(res)