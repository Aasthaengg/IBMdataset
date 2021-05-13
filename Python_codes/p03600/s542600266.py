N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

flag = [[True] * N for _ in range(N)]

for i in range(N):
    for j in range(i+1, N):
        for k in range(N):
            if k == i or k == j:
                continue
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            elif A[i][j] == A[i][k] + A[k][j]:
                flag[i][j] = False

ans = 0

for i in range(N):
    for j in range(i+1, N):
        if flag[i][j]:
            ans += A[i][j]

print(ans)