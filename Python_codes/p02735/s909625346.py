def main():
    H, W = map(int, input().split())
    s = [input() for _ in range(H)]

    dp = [[1 << 60] * W for _ in range(H)]

    dp[0][0] = int(s[0][0] == '#')

    for r in range(H):
        for c in range(W):
            t = dp[r][c]
            if r > 0:
                t = min(t, dp[r - 1][c] + int(s[r - 1][c] == '.' and s[r][c] == '#'))
            if c > 0:
                t = min(t, dp[r][c - 1] + int(s[r][c - 1] == '.' and s[r][c] == '#'))
            dp[r][c] = t

    print(dp[H - 1][W - 1])


if __name__ == '__main__':
    main()
