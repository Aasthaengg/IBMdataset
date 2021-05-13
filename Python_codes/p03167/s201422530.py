#!python3

LI = lambda: list(map(int, input().split()))

# input
H, W = LI()
A = [input() for _ in range(H)]

MOD = 10 ** 9 + 7


def main():
    dp = [[0] * W for _ in range(H)]
    for i in range(H):
        if A[i][0] == "#":
            break
        dp[i][0] = 1
    for j in range(W):
        if A[0][j] == "#":
            break
        dp[0][j] = 1
    for i in range(1, H):
        for j in range(1, W):
            if A[i - 1][j] == ".":
                dp[i][j] = dp[i - 1][j]
            if A[i][j - 1] == ".":
                dp[i][j] = (dp[i][j] + dp[i][j - 1]) % MOD
    ans = dp[-1][-1]
    print(ans)


if __name__ == "__main__":
    main()
