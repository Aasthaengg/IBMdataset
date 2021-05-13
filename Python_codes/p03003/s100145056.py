import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    S = list(map(int, readline().split()))
    T = list(map(int, readline().split()))

    dp = [1] * (M + 1)

    for i in range(N):
        dp_prev = dp[:]
        for j in range(M):
            if S[i] == T[j]:
                dp[j + 1] = (dp_prev[j + 1] + dp[j]) % MOD
            else:
                dp[j + 1] = (dp_prev[j + 1] + dp[j] - dp_prev[j]) % MOD

    print(dp[M])
    return


if __name__ == '__main__':
    main()
