string_n = input()
string_n = '0' + string_n
len_n = len(string_n)
dp = [[0, 0] for _ in range(len_n + 1)]

for i in range(len_n):
    for j in range(2):
        if j == 0:
            dp[i + 1][j] = min(dp[i]) + int(string_n[i])
        else:
            dp[i + 1][j] = min(dp[i][0] + 1 + 10 - int(string_n[i]), dp[i][1] + 9 - int(string_n[i]))

print(min(dp[len_n]))