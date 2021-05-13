import sys


def solve():
    readline = sys.stdin.buffer.readline
    mod = 10 ** 9 + 7
    n, t = list(map(int, readline().split()))
    ab = [list(map(int, readline().split())) for _ in range(n)]
    ab.sort()
    dp = [0] * t
    mv = 0
    for a, b in ab:
        mv = max(mv, dp[-1] + b)
        for i in range(t - 1 - a, -1, -1):
            dp[i+a] = max(dp[i+a], dp[i] + b)
    print(mv)


if __name__ == '__main__':
    solve()
