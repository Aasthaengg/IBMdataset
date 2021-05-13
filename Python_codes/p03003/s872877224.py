def main():
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    dp0 = [[0] * 2005 for _ in range(2005)]
    dp1 = [[0] * 2005 for _ in range(2005)]

    dp0[0][0] = 1
    for i in range(N + 1):
        for j in range(M + 1):
            dp0[i + 1][j] += dp0[i][j]
            dp1[i][j] += dp0[i][j]
            dp1[i][j] %= MOD
            dp1[i][j + 1] += dp1[i][j]
            if i < N and j < M and S[i] == T[j]:
                dp0[i + 1][j + 1] += dp1[i][j]
            dp1[i][j] %= MOD
            dp0[i + 1][j] %= MOD
            dp1[i][j + 1] %= MOD
            dp0[i + 1][j + 1] %= MOD

    ans = dp1[N][M] % MOD
    print (ans)
    return 

if __name__ == '__main__':
    main()