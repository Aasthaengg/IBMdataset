m = [[0, 4, 8, 12, 3, 7, 11, 2, 6, 10],[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],[0, 10, 7, 4, 1, 11, 8, 5, 2, 12],[0, 9, 5, 1, 10, 6, 2, 11, 7, 3],[0, 12, 11, 10, 9, 8, 7, 6, 5, 4],[0, 3, 6, 9, 12, 2, 5, 8, 11, 1]]
S = list(input())
d = len(S)
dp = [[0] * 13 for _ in range(d)]
if S[0] == '?':
    for x in m[d%6]:
        dp[0][x] = 1
else:
    dp[0][m[d%6][int(S[0])]] = 1
for i in range(1,d):
    if S[i] == '?':
        for j in range(13):
            dp[i][j] = sum(dp[i-1][(13+j-x) % 13] for x in m[(d-i)%6]) % 1000000007
    else:
        for j in range(13):
            dp[i][j] = dp[i-1][(13+j-m[(d-i)%6][int(S[i])])%13]
print(dp[d-1][5])