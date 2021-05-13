H, W = map(int, input().split())

field = []

for _ in range(H):
    field.append(input())

dp = [[0 for a in range(W)] for b in range(H)]
dp[0][0] = 1

# dp[h][w] = マス[1, 1]からマス[h, w]までの太郎くんの経路のそうパターン数。ans = dp[H-1][W-1]

for h in range(H):
    for w in range(W):
        if field[h][w] == '#': continue

        if h-1 >= 0 and field[h-1][w] == ".":
            dp[h][w] += dp[h-1][w]

        if w-1 >= 0 and field[h][w-1] == '.':
            dp[h][w] += dp[h][w-1]

        dp[h][w] %= 1000000007

print(dp[H-1][W-1])