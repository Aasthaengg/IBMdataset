N, K = map(int, input().split())
MOD = 10**9+7
cmb = [[1] if i == -1 else [1] + [0]*i + [1] for i in range(-1,N)]

for i in range(2, N+1):
    for j in range(1, i):
        cmb[i][j] = cmb[i-1][j-1] + cmb[i-1][j]

for i in range(1, K+1):
    try:
        ans = cmb[N-K+1][i]
    except IndexError:
        ans = 0
    if ans:
        ans *= cmb[K-1][i-1]
    print(ans % MOD)