def solve():
    MOD = 10 ** 9 + 7
    H, W = map(int,input().split())
    a = [list(input()) for _ in range(H)]
    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1

    for h in range(H):
        for w in range(W):
            if w-1 >= 0 and a[h][w-1] == '.':
                dp[h][w] += dp[h][w-1] % MOD
            if h-1 >= 0 and a[h-1][w] == '.':
                dp[h][w] += dp[h-1][w] % MOD

    print(dp[-1][-1] % MOD)
if __name__ == '__main__':
    solve()