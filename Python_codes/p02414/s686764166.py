N,M,L = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
B = [list(map(int,input().split())) for _ in range(M)]
C = [[0]*L for _ in range(N)]
for i in range(N):
    for j in range(L):
        num = 0
        for k in range(M):
            num += A[i][k] * B[k][j]
        C[i][j] = num
for l in range(N):
    print(*C[l])
