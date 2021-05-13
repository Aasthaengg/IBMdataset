# dp answer
N = int(input())
dp = [N for i in range(N+1)]
dp[0] = 0
Y = [1] + [6**i for i in range(1, 10) if 6**i <= N] + [9**i for i in range(1, 10) if 9**i <= N]
Y = sorted(Y)
for i in range(1, N+1):
    for y in Y:
        if i-y < 0:
            break
        dp[i] = min(dp[i], dp[i-y]+1)
print(dp[N])
