N, M = map(int, input().split())
X = []
Y = []
for _ in range(M):
    X.append(list(map(int, input().split())))
    
    tmp = 0
    for i in list(map(int, input().split())):
        tmp += 2 ** (i - 1)
    Y.append(tmp)

inf = 10 ** 9 + 7
dp = [[inf] * (2 ** N) for _ in range(M + 1)]
dp[0][0] = 0
for i in range(M):
    for j in range(2 ** N):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][j | Y[i]] = min(dp[i + 1][j | Y[i]],
                                  dp[i][j] + X[i][0])

ans = min(dp[i][-1] for i in range(M + 1))
print(ans if ans < inf else -1)

