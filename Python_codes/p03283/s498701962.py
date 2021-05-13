N, M, Q = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(M)]
pq = [list(map(int, input().split())) for _ in range(Q)]

matrix = [[0] * N for _ in range(N)]
for l, r in lr:
    l, r = l-1, r-1
    matrix[l][r] += 1

matrix2 = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if j == 0:
            matrix2[i][j] = matrix[i][j]
        else:
            matrix2[i][j] = matrix2[i][j-1] + matrix[i][j]

for p, q in pq:
    p, q = p-1, q-1
    count = 0
    for x in range(p, q + 1):
        count += matrix2[x][q]
    print(count)
