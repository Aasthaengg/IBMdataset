h, w = map(int, input().split())
m = [['#'] * (w+2) for i in range(h+2)]
for j in range(h):
    m[j+1][1:w+1] = list(input()) #適宜変える

dp = [[0 for i in range(w+2)] for j in range(h+2)]

dp[1][1] = 1

for i in range(1, h+1):
    for j in range(1, w+1):
        if m[i-1][j] == '.':
            dp[i][j] += dp[i-1][j]
        if m[i][j-1] == '.':
            dp[i][j] += dp[i][j-1]

print(dp[h][w] % 1000000007)