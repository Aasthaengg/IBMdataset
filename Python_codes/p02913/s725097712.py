import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N = int(readline())
    S = readline().strip()

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if S[i] == S[j]:
                dp[i][j] = dp[i + 1][j + 1] + 1

    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            if ans < min(dp[i][j], j - i):
                ans = min(dp[i][j], j - i)

    print(ans)
    return


if __name__ == '__main__':
    main()
