N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
B = [A[i][:] for i in range(N)]
C = [A[i][:] for i in range(N)]
for k in range(N):
    for i in range(N):
        for j in range(N):
            if k == i or k == j: continue
            if B[i][k]+B[k][j] <= B[i][j]:
                A[i][j] = -1
                B[i][j] = B[i][k]+B[k][j]

ans = 0
for i in range(N):
    for j in range(N):
        if B[i][j] != C[i][j]:
            print(-1)
            exit()
        if A[i][j] != -1:
            ans += A[i][j]
            A[i][j] = -1
            A[j][i] = -1
print(ans)