from copy import deepcopy
INF = 10 ** 10
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(int,input().split())))


L = []
for i in range(N-1):
    for j in range(i+1, N):
        L.append((A[i][j], i, j))
L.sort()

B = deepcopy(A)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if B[i][k] != 0 and B[k][j] != 0 and B[i][j] == B[i][k] + B[k][j]:
                B[i][j] = INF

ans = 0
for i in range(N):
    for j in range(N):
        if B[i][j] != INF:
            ans += B[i][j]
ans //= 2

for k in range(N):
    for i in range(N):
        for j in range(N):
            B[i][j] = min(B[i][j], B[i][k] + B[k][j])

if A == B:
    print(ans)
else:
    print(-1)