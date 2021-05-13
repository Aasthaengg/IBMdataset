import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = list(map(int, readline().split()))

    a = [0] * m
    c = [0] * m

    for i in range(m):
        a[i], _ = list(map(int, readline().split()))
        t = list(map(int, readline().split()))
        for x in t:
            c[i] += (1 << (x - 1))

    dp = [[INF] * (1 << n) for _ in range(m)]
    dp[0][c[0]] = a[0]

    for i in range(m):
        dp[i][0] = 0

    for i in range(1, m):
        key = c[i]
        price = a[i]
        for j in range(1 << n):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if dp[i - 1][j] != INF:
                dp[i][j | key] = min(dp[i][j | key], dp[i - 1][j] + price)

    ans = dp[-1][-1]
    if ans == INF:
        ans = -1
    print(ans)


if __name__ == '__main__':
    main()
