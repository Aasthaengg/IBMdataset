n, m = map(int, input().split())
A, B = [list(map(int, input().split())) for r in range(n)], [list(map(int, input().split())) for r in range(m)]
for i in range(n):
    Ci = 0
    for j in range(m):
        Ci += A[i][j] * B[j][0]
    print(Ci)