N, M, X = map(int, input().split())
C = [list(map(int, input().split())) for i in range(N)]
ans = -1
for i in range(2 ** N):
    rikaido = [0 for k in range(M)]
    kingaku = 0
    for j in range(N):
        if ((i >> j) & 1):
            for k in range(M):
                rikaido[k] += C[j][k + 1]
            kingaku += C[j][0]
    if (min(rikaido) >= X) and (ans > kingaku or ans == -1):
        ans = kingaku
print(ans)