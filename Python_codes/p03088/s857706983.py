def resolve():
    N = int(input())
    
    def isOk(i3, i2, i1, i0):
        if i2 == 0 and i1 == 1 and i0 == 2: return False
        if i2 == 1 and i1 == 0 and i0 == 2: return False
        if i2 == 0 and i1 == 2 and i0 == 1: return False
        if i3 == 0 and i1 == 1 and i0 == 2: return False
        if i3 == 0 and i2 == 1 and i0 == 2: return False
        return True
     
    dp = [[[[0 for _ in range(4)] for __ in range(4)] for ___ in range(4)] for ____ in range(N+1)]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if isOk(None, i, j, k):
                    dp[3][i][j][k] = 1

    for n in range(3, N):
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    for l in range(4):
                        if not isOk(i, j, k, l):
                            continue
                        dp[n+1][j][k][l] += dp[n][i][j][k]
                        dp[n+1][j][k][l] %= (10**9)+7

    total = 0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                total += dp[N][i][j][k]
                total %= (10**9)+7
    print(total)


if '__main__' == __name__:
    resolve()