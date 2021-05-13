h,w=map(int,input().split())
a = [input() for _ in range(h)]
dp = [[0 for _ in range(w)]for __ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0: continue
        if a[i][j] == '#':continue
        if i == 0:
            dp[i][j] = dp[i][j-1]
        elif j == 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            dp[i][j] %= 1000000007
print(dp[h-1][w-1])