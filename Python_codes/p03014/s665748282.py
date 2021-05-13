H, W = map(int, input().split(' '))

S = [input() for _ in range(H)]

rows = []
cols = []

for y in range(H):
    cont = 0
    row = []
    for x in range(W):
        if S[y][x] == '.':
            cont += 1
        else:
            for _ in range(cont):
                row.append(cont)
            row.append(0)
            cont = 0
    for _ in range(cont):
        row.append(cont)
    rows.append(row)

for x in range(W):
    cont = 0
    col = []
    for y in range(H):
        if S[y][x] == '.':
            cont += 1
        else:
            for _ in range(cont):
                col.append(cont)
            col.append(0)
            cont = 0
    for _ in range(cont):
        col.append(cont)
    cols.append(col)

ans = 0
for y in range(H):
    for x in range(W):
        if S[y][x] == '.':
            ans = max(ans, rows[y][x] + cols[x][y] - 1)

print(ans)
