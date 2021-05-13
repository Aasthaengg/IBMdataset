N = int(input())
abc = []
for i in range(N):
    abc.append(list(map(int,input().split())))
dp = [[0,0,0] for _ in range(N)]
dp[0] = abc[0][:]
for i in range(1,N):
    dp[i][0] = abc[i][0] + max(dp[i-1][1],dp[i-1][2])
    dp[i][1] = abc[i][1] + max(dp[i-1][0],dp[i-1][2])
    dp[i][2] = abc[i][2] + max(dp[i-1][1],dp[i-1][0])
print(max(dp[-1]))