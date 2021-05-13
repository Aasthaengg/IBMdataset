n, m, l = map(int, input().split())
A = [[int(n) for n in input().split()] for i in range(n)]
B = [[int(n) for n in input().split()] for i in range(m)]
C = [[0 for i in range(l)] for i in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]
for i in range(n):
    for j in range(l):
        if j == l - 1:
            print(C[i][j])
        else:
            print(C[i][j], end = " ")