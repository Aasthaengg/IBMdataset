def main():
    MOD = 10 ** 9 + 7
    H, W = list(map(int, input().split(' ')))
    A = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    for w in range(W):
        if A[0][w] == '#':
            break
        dp[0][w] = 1
    for h in range(H):
        if A[h][0] == '#':
            break
        dp[h][0] = 1
    for h in range(1, H):
        for w in range(1, W):
            if A[h][w] == '#':
                continue
            dp[h][w] = (dp[h - 1][w] + dp[h][w - 1]) % MOD
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
