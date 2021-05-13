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
        C[i] = ~sum(1 << (int(s) - 1) for s in readline().split())

    dp = [INF] * (1 << N)
    dp[0] = 0
    for bit in range(1 << N):
        for a, c in zip(A, C):
            if dp[bit & c] < INF:
                dp[bit] = min(dp[bit], dp[bit & c] + a)

    ans = dp[(1 << N) - 1]
    if ans < INF:
        print(ans)
    else:
        print(-1)
    return


if __name__ == '__main__':
    main()
