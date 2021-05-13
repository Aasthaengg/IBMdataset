n, m, l = map(int, input().split())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
for _ in range(m):
    B.append(list(map(int, input().split())))
C = [[0 for _ in range(l)] for _ in range(n)]
for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += A[i][k] * B[k][j]
        C[i][j] = s

for row in C:
    print(' '.join(list(map(str, row))))

