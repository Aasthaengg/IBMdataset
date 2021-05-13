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

    dp = [0] * (N + 1)
    ans = 0

    for i in range(N - 1, -1, -1):
        for j in range(i + 1, N):
            dp[j] = dp[j + 1] + 1 if S[i] == S[j] else 0
            if ans < min(dp[j], j - i):
                ans = min(dp[j], j - i)

    print(ans)
    return


if __name__ == '__main__':
    main()
