h, w = map(int, input().split())
s = [input() for _ in range(h)]

# 準備
row = [[0] * w for _ in range(h)]
col = [[0] * w for _ in range(h)]
for i in range(h):
    prev_wall = -1
    for j in range(w + 1):
        if j == w:
            for k in range(prev_wall+1, j):
                row[i][k] = j - prev_wall - 1
        elif s[i][j] == '#' and j - prev_wall > 0:
            for k in range(prev_wall+1, j):
                row[i][k] = j - prev_wall - 1
            prev_wall = j

for j in range(w):
    prev_wall = -1
    for i in range(h + 1):
        if i == h:
            for k in range(prev_wall+1, i):
                col[k][j] = i - prev_wall - 1
        elif s[i][j] == '#' and i - prev_wall > 0:
            for k in range(prev_wall+1, i):
                col[k][j] = i - prev_wall - 1
            prev_wall = i

# 全探索
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, row[i][j] + col[i][j] - 1)
print(ans)
