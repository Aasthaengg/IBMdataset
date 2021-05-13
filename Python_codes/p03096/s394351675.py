import sys

sys.setrecursionlimit(10 ** 6)
INF = float("inf")
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().strip()


def main():
    N = int(input())
    C = [int(input()) for _ in range(N)] + [-1]
    C = [C[i] for i in range(N) if C[i] != C[i + 1]]

    N = len(C)
    # dp[i] := i個までの色の塗り方の総和
    dp = [0] * N
    dp[0] = 1
    used = [-1] * (max(C) + 1)
    used[C[0]] = 0

    for i in range(1, N):
        if used[C[i]] == -1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = dp[i - 1] + dp[used[C[i]]]

        dp[i] %= MOD
        used[C[i]] = i

    print(dp[-1])


if __name__ == "__main__":
    main()
