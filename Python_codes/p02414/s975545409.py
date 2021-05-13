n, m, l = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
matrix2 = [list(map(int, input().split())) for _ in range(m)]
table = [[0]*l for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            table[i][j] += matrix1[i][k] * matrix2[k][j]
for row in table:
    print(' '.join(map(str, row)))
