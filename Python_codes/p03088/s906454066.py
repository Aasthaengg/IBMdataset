import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    # dp[i][j][k][l] := 長さiの文字において，後ろから3つ目の文字がj,
    # 後ろから2つ目の文字がk, 後ろから1つの文字がlの時の組み合わせ数
    dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]

    A = 1
    G = 2
    C = 3
    T = 4

    # 文字の意味は，0 => None, 1 => A, 2 => G, 3 => C, 4 => T
    dp[0][0][0][0] = 1
    for i in range(1, N + 1):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(1, 5):
                        if k == A and l == G and m == C:
                            continue
                        if k == A and l == C and m == G:
                            continue
                        if k == G and l == A and m == C:
                            continue
                        if j == A and l == G and m == C:
                            continue
                        if j == A and k == G and m == C:
                            continue

                        dp[i][k][l][m] += dp[i - 1][j][k][l]
                        dp[i][k][l][m] %= MOD

    ans = 0
    for j in range(1, 5):
        for k in range(1, 5):
            for l in range(1, 5):
                ans += dp[-1][j][k][l]
                ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
