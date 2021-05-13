r, c = map(int, input().split())
a = [[int(i) for i in input().split()] for j in range(r)]
b = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
    for j in range(c):
        b[i][j] = a[i][j]
        b[i][c] += a[i][j]
    
for i in range(c+1):
    for j in range(r):
        b[r][i] += b[j][i]

for i in range(r+1):
    for j in range(c+1):
        if j == c:
            print(b[i][j])
        else:
            print("{0} ".format(b[i][j]), end = "")