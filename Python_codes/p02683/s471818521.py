N, M, X = map(int, input().split())
C = []*N
A = []
for i in range(N):
    b = list(map(int, input().split()))
    C.append(b[0])
    A.append(b[1:])
ans = -1
for i in range(2**N):
    t = [0] * M
    c = 0
    for j in range(N):
        if (i >> j) & 1 == 0:
            continue
        c += C[j]
        for k in range(M):
            t[k] += A[j][k]
    if all(x >= X for x in t):
        if ans == -1:
            ans = c
        else:
            ans = min(ans, c)
print(ans)