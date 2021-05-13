r, c = map(int, input().split())
a = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    l = list(map(int, input().split()))
    for j in range(c):
        a[i][j] = l[j]
        a[i][c] += a[i][j]

for i in range(c+1):
    for j in range(r):
        a[r][i] += a[j][i]

for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(str(a[i][j]))
        else:
            print(str(a[i][j]) + " ", end="")