r, c = map(int, input().split())
a = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    j = 0
    for line in input().split():
        a[i][j] = int(line)
        a[i][c] += a[i][j]
        j += 1
for i in range(c+1):
    for j in range(r):
        a[r][i] += a[j][i]
for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(a[i][j])
        else:
            print(a[i][j], end=" ")