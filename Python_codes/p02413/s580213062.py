r, c = map(int, input().split())

d = [0] * (r + 1)

for i in range(r):
    d[i] = list(map(int, input().split()))
    d[i].append(0)
    for j in range(c):
        d[i][c] += d[i][j]

d[r] = [0] * (c + 1)
for i in range(c + 1):
    for j in range(r):
        d[r][i] += d[j][i]

for i in range(r + 1):
    row = ''
    for j in range(c + 1):
        row += str(d[i][j])
        if j <= c - 1:
            row += ' '
    print(row)

