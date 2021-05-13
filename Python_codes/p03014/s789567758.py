h, w = map(int, input().split())
s = [input() for _ in range(h)]
hrz = [[0] * w for _ in range(h)]
vrt = [[0] * w for _ in range(h)]
for i in range(h):
    cnt = 0
    for j in range(w + 1):
        if j < w and s[i][j] == '.':
            if cnt == 0:
                start = j
            cnt += 1
        elif cnt > 0:
            for k in range(start, j):
                hrz[i][k] = cnt
            cnt = 0
for j in range(w):
    cnt = 0
    for i in range(h + 1):
        if i < h and s[i][j] == '.':
            if cnt == 0:
                start = i
            cnt += 1
        elif cnt > 0:
            for k in range(start, i):
                vrt[k][j] = cnt
            cnt = 0
ans = max(hrz[i][j] + vrt[i][j] - 1 for i in range(h) for j in range(w))
print(ans)
