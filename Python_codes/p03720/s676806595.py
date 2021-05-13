N, M = map(int, input().split())
A = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    A[a][b] += 1
    A[b][a] += 1
for i in range(1, N+1):
    sum = 0
    for j in range(1, N+1):
        sum += A[i][j]
    print(sum)