N = int(input())
abc = []
for i in range(N):
    data = list(map(int, input().split()))
    abc.append(data)

dp = [[0 for i in range(3)] for j in range(N)]
dp[0][0] = abc[0][0]
dp[0][1] = abc[0][1]
dp[0][2] = abc[0][2]

for i in range(N-1):
    for j in range(3):
        if j == 0:
            dp[i+1][1] = max(dp[i][0] + abc[i+1][1], dp[i+1][1])
            dp[i+1][2] = max(dp[i][0] + abc[i+1][2], dp[i+1][2])
        if j == 1:
            dp[i+1][0] = max(dp[i][1] + abc[i+1][0], dp[i+1][0])
            dp[i+1][2] = max(dp[i][1] + abc[i+1][2], dp[i+1][2])
        if j == 2:
            dp[i+1][1] = max(dp[i][2] + abc[i+1][1], dp[i+1][1])
            dp[i+1][0] = max(dp[i][2] + abc[i+1][0], dp[i+1][0])

print(max(dp[N-1]))