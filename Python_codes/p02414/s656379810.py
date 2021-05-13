n, m, l = [int(x) for x in input().split(' ')]

A = [0] * n
for i in range(n):
    A[i] = [int(x) for x in input().split(' ')]
B = [0] * m
for i in range(m):
    B[i] = [int(x) for x in input().split(' ')]

def tranpose(matrix):
    r, c = len(matrix), len(matrix[0])
    return [[row[i] for row in matrix] for i in range(c)]

B = tranpose(B)
C = [[0 for _ in range(l)] for _ in range(n)]

for i in range(n):
    for j in range(l):
        C[i][j] =  sum(a * b for a, b in zip(A[i], B[j]))

for row in C:
    print(*row, sep=' ')