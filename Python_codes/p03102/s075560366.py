N, M, C = [int(a) for a in input().split()]
B = [int(a) for a in input().split()]
A = []
for _ in range(N):
    A_ = [int(a) for a in input().split()]
    A.append(A_)

ans = 0

for i in range(N):
    r = C
    for j in range(M):
        r += A[i][j]*B[j]
    if r > 0:
        ans += 1

print(ans)
