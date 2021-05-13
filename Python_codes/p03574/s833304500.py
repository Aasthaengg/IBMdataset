h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

di = [1, -1, 0, 0, 1, -1, 1, -1]
dj = [0, 0, 1, -1, 1, -1, -1, 1]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue
        cnt = 0
        for ii, jj in zip(di, dj):
            ni = i + ii
            nj = j + jj
            if 0 <= ni < h and 0 <= nj < w:
                if s[ni][nj] == '#':
                    cnt += 1
        s[i][j] = chr(ord('0') + cnt)

for x in s:
    print(''.join(x))
