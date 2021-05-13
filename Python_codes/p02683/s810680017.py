N, M, X = map(int, input().split())
C = []
A = []
for i in range(N):
    l = list(map(int, input().split()))
    C.append(l[0])
    A.append(l[1:])

mn = 1e9
for i in range(2 ** N):
    p = [0] * M
    v = 0
    for j in range(N):
        if (1 << j) & i:
            v += C[j]
            for k in range(M):
                p[k] += A[j][k]
    if min(p) >= X:
        mn = min(mn, v)
print(mn if mn != 1e9 else -1)