N, K = map(int, input().split())
MOD = 10 **9 + 7
C = [[0] * (N + 1) for i in range(N + 1)]
C[1][1] = 1
for i in range(2, N + 1):
    for j in range(1, i + 1):
        if j == 1:
            C[i][j] = C[i - 1][j] + 1
        elif j == i:
            C[i][j] = 1
        else:
            C[i][j] = C[i - 1][j - 1] + C[i - 1][j]
print(N - K + 1)
for i in range(2, K + 1):
    ans = (C[N - K + 1][i] * C[K - 1][i - 1]) % MOD
    print(ans)