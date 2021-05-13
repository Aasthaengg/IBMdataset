import sys
import collections

sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline


def main():
    H, W = [int(x) for x in input().split()]
    S = [list(input().strip()) for _ in range(H)]

    dp = [[10 ** 9] * W for j in range(H)]

    if S[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for j in range(H):
        for i in range(W):
            if j != H - 1:
                x = 1 if S[j + 1][i] == '#' and S[j][i] == '.' else 0
                dp[j + 1][i] = min(dp[j + 1][i], dp[j][i] + x)
            if i != W - 1:
                x = 1 if S[j][i + 1] == '#' and S[j][i] == '.' else 0
                dp[j][i + 1] = min(dp[j][i + 1], dp[j][i] + x)

    print(dp[-1][-1])


if __name__ == '__main__':
    main()
