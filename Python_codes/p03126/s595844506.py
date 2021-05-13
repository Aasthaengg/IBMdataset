N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
L = [0] * M
for i in range(N):
    for j in range(1, A[i][0] + 1):
        L[ A[i][j] -1 ] += 1
print(L.count(N))
