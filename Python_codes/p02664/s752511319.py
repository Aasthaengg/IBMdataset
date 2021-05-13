def solve():
    INF = float('inf')
    P = 0
    D = 1

    Ts = input().rstrip()

    N = len(Ts)

    dp = [[-INF]*(2) for _ in range(N+1)]
    dp[0][D] = 0
    prevss = [[-1]*(2) for _ in range(N+1)]
    for i, T in enumerate(Ts, start=1):
        if T == 'P' or T == '?':
            dpP = dp[i-1][P]
            dpD = dp[i-1][D]
            if dpP >= dpD:
                dp[i][P] = dpP
                prevss[i][P] = P
            else:
                dp[i][P] = dpD
                prevss[i][P] = D
        if T == 'D' or T == '?':
            dpP = dp[i-1][P] + 2
            dpD = dp[i-1][D] + 1
            if dpP >= dpD:
                dp[i][D] = dpP
                prevss[i][D] = P
            else:
                dp[i][D] = dpD
                prevss[i][D] = D

    #for i in range(N+1):
    #    print(dp[i], Ts[i-1])

    if dp[-1][P] >= dp[-1][D]:
        j = P
    else:
        j = D
    anss = [j]
    for i in reversed(range(2, N+1)):
        j = prevss[i][j]
        anss.append(j)
    #print(anss)

    anss = ''.join(['P' if ans == P else 'D' for ans in anss[::-1]])
    print(anss)


solve()
