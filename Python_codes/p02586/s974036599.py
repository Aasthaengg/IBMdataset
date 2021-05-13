R,C,K = map(int,input().split())
items = [[0]*(C+1) for _ in range(R+1)]
for i in range(K):
    r,c,v = map(int,input().split())
    items[r][c] = v

dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]

for y in range(R+1):
    for x in range(C+1):
        for i in range(4):
            position = dp[i][y][x]
            if y+1 <= R:
                dp[0][y+1][x] = max(dp[0][y+1][x], position)
                dp[1][y+1][x] = max(dp[1][y+1][x], position+items[y+1][x])
            if x+1 <= C:
                dp[i][y][x+1] = max(dp[i][y][x+1], position)
                if i < 3:
                    dp[i+1][y][x+1] = max(dp[i+1][y][x+1], position+items[y][x+1])

ans = 0
for i in range(4):
    ans = max(ans, dp[i][-1][-1])
print(ans)