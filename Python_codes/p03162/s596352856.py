N = int(input())
abc = [list(map(int,input().split())) for c in range(N)]
dp = [[0,0,0] for c in range(N)]
dp[0] = [abc[0][0],abc[0][1],abc[0][2]]
for i in range(1,N):
    for j in range(3):
        # print([dp[i-1][c] + abc[i][j] for c in range(3) if c != j])
        dp[i][j] = max([dp[i-1][c] + abc[i][j] for c in range(3) if c != j])
        # print(dp[i][j])

print(max([dp[N-1][i] for i in range(3)]))
