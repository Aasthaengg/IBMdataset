h,w = map(int,input().split())
stage = [["#" for x in range(w+2)] for x in range(h+2)]
for i in range(1,h+1):
    stage[i][1:w+1] = list(input())
dp = [[0 for x in range(w+2)] for x in range(h+2)]
dp[1][1] = 1
for j in range(1,h+1):
    for i in range(1,w+1):
        dp[j][i] = dp[j][i]%(10**9+7)
        if(stage[j+1][i] == "."):
            dp[j+1][i] += dp[j][i]
        if(stage[j][i+1] == "."):
            dp[j][i+1] += dp[j][i]
print(dp[h][w])
