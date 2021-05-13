def main():
    H, W = list(map(int, input().split()))
    dp = [['0'] * (W + 2)] + [['0', ] + ['0' if a == '#' else a for a in list(input())] + ['0', ] for _ in range(H)] + [['0'] * (W + 2)]
    mod = 1000000007
    dp[1][1] = '1'
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if dp[h][w] == '.':
                dp[h][w] = str((int(dp[h - 1][w]) + int(dp[h][w - 1])) % mod)
    print(dp[H][W])

if __name__ == '__main__':
    main()
