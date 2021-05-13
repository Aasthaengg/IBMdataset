N = int(input())
a = [list(map(int, input().split())) for i in range(N)]

dp = [[0 for i in range(3)] for j in range(N)]
dp[0][0] = a[0][0]
dp[0][1] = a[0][1]
dp[0][2] = a[0][2]

for i in range(1, N):
    for place in range(3):
        for place_y in range(3):
            if place == place_y:
                continue
            dp[i][place] = max(dp[i][place], dp[i-1][place_y]+a[i][place])


print(max(dp[N-1]))
