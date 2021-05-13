n, m, l = map(int, raw_input().split())

A = [map(int, raw_input().split()) for i in range(n)]
B = [map(int, raw_input().split()) for i in range(m)]

C = [[sum(A[i][k]*B[k][j] for k in range(m)) for j in range(l)] for i in range(n)]

for row in C:
    print " ".join(map(str, row))