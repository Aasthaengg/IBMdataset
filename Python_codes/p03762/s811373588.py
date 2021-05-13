import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = map(int, readline().split())
    x = list(map(int, readline().split()))
    y = list(map(int, readline().split()))

    s = 0

    for i in range(1, m):
        s += i * (m - i) * (y[i] - y[i - 1])
        s %= MOD

    ans = 0

    for i in range(1, n):
        t = s * (x[i] - x[i - 1])
        t %= MOD
        t *= i * (n - i)
        t %= MOD
        ans += t
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
