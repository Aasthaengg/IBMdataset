N, M, X = map(int, input().split())

C = [0] * N
A = [0] * N
for i in range(N):
    ca = list(map(int, input().split()))
    C[i] = ca[0]
    A[i] = ca[1:]

ans = 10**11
for i in range(2**N):
    b = format(i, "0" + str(N) + "b")
    r = [0] * M
    c = 0
    for j in range(N):
        f = int(b[j])
        c += C[j] * f
        for k in range(M):
            r[k] += f * A[j][k]
        if min(r) >= X:
            ans = min(c, ans)

if ans == 10**11:
    print("-1")
else:
    print(ans)