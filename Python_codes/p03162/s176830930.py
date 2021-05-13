def main():
    n = int(input())
    abc = [[0, 0, 0] for _ in range(n + 1)]
    for i in range(1, n + 1):
        abc[i] = list(map(int, input().split()))
    dp = [[0, 0, 0] for _ in range(n + 1)]
    dp[1] = abc[1]

    for i in range(1, n + 1):
        for j in range(3):
            for k in range(3):
                if j == k:
                    continue
                dp[i][j] = max(dp[i][j], dp[i - 1][k] + abc[i][j])

    print(max(dp[-1]))


if __name__ == "__main__":
    main()
