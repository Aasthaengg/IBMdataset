import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, M = map(int, readline().split())
    A = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], b = map(int, readline().split())
        C[i] = sum(1 << (int(s) - 1) for s in readline().split())

    dp = [[INF] * (1 << N) for _ in range(M + 1)]
    dp[0][0] = 0
    for i in range(M):
        for j in range(1 << N):
            if dp[i + 1][j] > dp[i][j]:
                dp[i + 1][j] = dp[i][j]
            if dp[i + 1][j | C[i]] > dp[i][j] + A[i]:
                dp[i + 1][j | C[i]] = dp[i][j] + A[i]

    ans = dp[M][(1 << N) - 1]
    if ans < INF:
        print(ans)
    else:
        print(-1)
    return


if __name__ == '__main__':
    main()
