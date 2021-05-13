h, w = map(int, input().split())
s = [[] for _ in range(h)]

for i in range(h):
    s[i] = input()

cnt_ver = [[0] * w for _ in range(h)]
cnt_hor = [[0] * w for _ in range(h)]

# check vertical
for i in range(w):
    for j in range(h):
        if s[j][i] == "#":
            cnt_ver[j][i] = 0
        elif j - 1 < 0 or s[j - 1][i] == "#":
            cnt_ver[j][i] = 1
        else:
            cnt_ver[j][i] = cnt_ver[j - 1][i] + 1

for i in range(w):
    for j in range(h - 1, -1, -1):
        if s[j][i] == "#":
            continue
        elif j + 1 < h and cnt_ver[j + 1][i] != 0:
            cnt_ver[j][i] = cnt_ver[j + 1][i]

# check horizontal
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            cnt_hor[i][j] = 0
        elif j - 1 < 0 or s[i][j - 1] == "#":
            cnt_hor[i][j] = 1
        else:
            cnt_hor[i][j] = cnt_hor[i][j - 1] + 1

for i in range(h):
    for j in range(w - 1, -1, -1):
        if s[i][j] == "#":
            continue
        elif j + 1 < w and cnt_hor[i][j + 1] != 0:
            cnt_hor[i][j] = cnt_hor[i][j + 1]

ans = 0

for i in range(h):
    for j in range(w):
        ans = max(ans, cnt_hor[i][j] + cnt_ver[i][j] - 1)

print(ans)
