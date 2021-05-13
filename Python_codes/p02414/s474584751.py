n, m, l = map(int, input().split())
A = [[0 for i in range(m)] for j in range(n)]
B = [[0 for i in range(l)] for j in range(m)]
C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    t = list(map(int, input().split()))
    for j in range(m):
        A[i][j] = t[j]

for i in range(m):
    t = list(map(int, input().split()))
    for j in range(l):
        B[i][j] = t[j]

for i in range(l):
    for j in range(n):
        for k in range(m):
            C[j][i] += A[j][k] * B[k][i]
for i in range(n):
    for j in range(l):
        if j == l - 1:
            print(str(C[i][j]))
        else:
            print(str(C[i][j]) + " ", end="")