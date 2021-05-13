N, M, X = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]

flg = False
ans = 10**9
for i in range(2**N):
    bits = bin(i)[2:].zfill(N)
    ok = True
    xs = [0] * M
    tmp = 0
    for i, b in enumerate(bits):
        if b == '0': continue

        for j in range(M):
            xs[j] += L[i][j+1]

        tmp += L[i][0]

    for x in xs:
        if x < X:
            ok = False
            break

    if ok:
        flg = True
        ans = min(tmp, ans)

ans = ans if flg else -1
print(ans)