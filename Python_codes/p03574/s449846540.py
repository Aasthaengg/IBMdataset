h, w = map(int, input().split())
s = [list(input()) for _ in range(0, h)]

dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [1, 0, -1, 1, -1, 1, 0, -1]

for i in range(0, h):
    for j in range(0, w):
        if s[i][j] != '.':
            continue

        cnt = 0
        for k in range(0, 8):
            ni = i + dy[k]
            nj = j + dx[k]

            if not (ni < 0 or h <= ni) and not (nj < 0 or w <= nj) and s[ni][nj] == '#':
                cnt += 1

        s[i][j] = str(cnt)

[print(''.join(s[ii])) for ii in range(0, h)]
