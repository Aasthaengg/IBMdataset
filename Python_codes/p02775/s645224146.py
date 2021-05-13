INF = 10**18

S = '0'+input()
N = len(S)

dp = [[INF,INF] for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for j in range(2):
        s = int(S[-1-i])
        s += j

        for a in range(10):
            ni = i+1
            nj = 0
            b = a-s
            if b < 0:
                b += 10
                nj = 1
            dp[ni][nj] = min(dp[ni][nj],dp[i][j]+a+b)

print(dp[N][0])