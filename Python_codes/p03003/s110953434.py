N, M = map(int, input().split())
S = list(map(int, input().split()))
S.append(-1)
T = list(map(int, input().split()))
T.append(0)
mod = 10 ** 9 + 7
dp0 = [[0] * 2005 for _ in range(2005)]
dp1 = [[0] * 2005 for _ in range(2005)]
dp0[0][0] = 1
for i in range(N + 1):
    for j in range(M + 1):
        dp0[i + 1][j] += dp0[i][j] % mod
        dp1[i][j] += dp0[i][j] % mod
        dp1[i][j + 1] += dp1[i][j] % mod
        if S[i] == T[j]:
            dp0[i + 1][j + 1] += dp1[i][j] % mod
ans = dp1[N][M] % mod
print(ans)