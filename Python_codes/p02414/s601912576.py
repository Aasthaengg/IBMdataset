n, m, l = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
B = [list(map(int, input().split())) for _ in range(m)]
for i in range(n):
    r = []
    for j in range(l):
        c = 0
        for k in range(m):
            c += A[i][k] * B[k][j]
        r.append(c)
    print(*r) 