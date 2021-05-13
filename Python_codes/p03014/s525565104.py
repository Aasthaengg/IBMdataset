h, w = map(int, input().split())
data = [list(input()) for _ in range(h)]

cnt_l, cnt_r, cnt_u, cnt_d = [[0] * w for _ in range(h)], [[0] * w for _ in range(h)], [[0] * w for _ in range(h)], [[0] * w for _ in range(h)]

for i in range(h):
    for j in range(w):
        if data[i][j] == "#":
            cnt_l[i][j] = 0
        else:
            cnt_l[i][j] = cnt_l[i][j - 1] + 1
    
        if data[i][w - j - 1] == "#":
            cnt_r[i][w - j - 1] = 0
        else:
            if j == 0:
                cnt_r[i][w - j - 1] = 1
            else:
                cnt_r[i][w - j - 1] = cnt_r[i][w - j] + 1

for j in range(w):
    for i in range(h):
        if data[i][j] == "#":
            cnt_u[i][j] = 0
        else:
            cnt_u[i][j] = cnt_u[i - 1][j] + 1

        if data[h - i - 1][j] == "#":
            cnt_d[h - i - 1][j] = 0
        else:
            if i == 0:
                cnt_d[h - i - 1][j] = 1
            else:
                cnt_d[h - i - 1][j] = cnt_d[h - i][j] + 1

ans = 0
for i in range(h):
    for j in range(w):
        total= cnt_l[i][j] + cnt_r[i][j] + cnt_u[i][j] + cnt_d[i][j] - 3
        ans = max(ans, total)

print(ans)