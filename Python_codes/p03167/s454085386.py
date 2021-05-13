MOD = 10**9 + 7


def main():
    # もらうDP
    H, W = (int(i) for i in input().split())
    c = [input() for i in range(H)]
    dp = [[0]*W for i in range(H)]

    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            le = 0
            up = 0
            if 0 <= w - 1 and c[h][w-1] != "#":
                le = dp[h][w-1]
            if 0 <= h - 1 and c[h-1][w] != "#":
                up = dp[h-1][w]
            dp[h][w] += le + up
            dp[h][w] %= MOD
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
