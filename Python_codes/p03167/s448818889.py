mod = 10**9+7


def main():
    H, W = map(int, input().split())
    a = [input() for _ in range(H)]
    dp = [[0 for _ in range(W)] for _ in range(H)]
    dp[0][0] = 1
    for i in range(H):
        for j in range(W):
            if i != 0 or j != 0:
                if a[i][j] == ".":
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    dp[i][j] %= mod
    print(dp[-1][-1])


if __name__ == "__main__":
    main()
