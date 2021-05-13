import copy

N = int(input())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

B = copy.deepcopy(A)
for i in range(N):
    for j in range(i, N):
        for k in range(N):
            if not (i != j and j != k and k != i):
                continue
            if A[i][j] > A[i][k] + A[k][j]:
                print(-1)
                exit()
            if A[i][j] == A[i][k] + A[k][j]:
                B[i][j] = 0

ans = 0
for i in range(N):
    for j in range(i, N):
        ans += B[i][j]

print(ans)

