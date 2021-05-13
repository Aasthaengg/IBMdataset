N = int(input())
abc = [list(map(int, input().split())) for _ in range(N)]

dp = [[0, 0, 0]] * N
dp[0] = abc[0]

for i in range(1, N):
    tmp1 = max(dp[i-1][1]+abc[i][0], dp[i-1][2]+abc[i][0])
    tmp2 = max(dp[i-1][0]+abc[i][1], dp[i-1][2]+abc[i][1])
    tmp3 = max(dp[i-1][0]+abc[i][2], dp[i-1][1]+abc[i][2])
    dp[i] = [tmp1, tmp2, tmp3]
print(max(dp[N-1]))

