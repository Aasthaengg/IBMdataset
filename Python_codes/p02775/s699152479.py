s = input()
keta = len(s)
infi = 10 ** 10
dp = [[infi] * (2) for _ in range(keta + 1)]
dp[0][0] = 0
s = s[::-1]
for i in range(keta):
    for j in range(2):
        num = int(s[i])
        if j == 1:
            num += 1
        ni = i + 1
        if num == 10:
            nj = 1
            num = 0
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + num)
        elif num < 5:
            nj = 0
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + num)
        elif num > 5:
            nj = 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 10 - num)
        else:
            nj = 0
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + num)
            nj = 1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 10 - num)
print(min(dp[keta][0], dp[keta][1] + 1))
