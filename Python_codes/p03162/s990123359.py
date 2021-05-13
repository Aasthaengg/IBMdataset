n = int(input())
abc = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*3 for _ in range(n+1)]
#dp[i][a] := i日目にaするときの、i日目までの幸福度の最大値
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1] + abc[i-1][0],
                   dp[i-1][2] + abc[i-1][0])
    dp[i][1] = max(dp[i-1][0] + abc[i-1][1],
                   dp[i-1][2] + abc[i-1][1])
    dp[i][2] = max(dp[i-1][0] + abc[i-1][2],
                   dp[i-1][1] + abc[i-1][2])
print(max(dp[n]))
