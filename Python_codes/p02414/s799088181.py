n, m, l = map(int, input().split(' '))

A = []
for i in range(n):
    A.append(list(map(int, input().split(' '))))


B = []
for i in range(m):
    B.append(list(map(int, input().split(' '))))

C = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            C[i][j] += A[i][k] * B[k][j]

for c in C:
    print(' '.join([str(x) for x in c]))