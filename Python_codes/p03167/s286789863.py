MOD = 10**9 + 7
H, W = map(int, input().split())
field = [['#'] * (W + 2)]
for i in range(H):
    field.append(list('#' + input() + '#'))
field.append(['#'] * (W + 2))

dp = [[0 for _ in range(W+2)] for _ in range(H+2)]
dp[H][W] = 1

for i in range(H,0,-1):
    for j in range(W,0,-1):
        if field[i][j] == '#':
            continue
        else:
            dp[i][j] += dp[i][j+1] + dp[i+1][j]
        dp[i][j] %= MOD

print(dp[1][1])