N = int(input())
happy = [[0, 0, 0]]
for _ in range(N):
    happy.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N+1)]

for i in range(1,N+1):
    for today in range(3):
        for yesterday in range(3):
            if today == yesterday: continue

            dp[i][today] = max(dp[i][today], dp[i-1][yesterday] + happy[i][today])

print(max(dp[N][0], dp[N][1], dp[N][2]))