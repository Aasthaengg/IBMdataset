import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m = map(int, readline().split())
    diff = abs(n - m)

    if diff > 1:
        print(0)
    else:
        ans = n
        for i in range(1, n):
            ans *= i
            ans %= MOD
        for i in range(1, m + 1):
            ans *= i
            ans %= MOD

        if diff == 0:
            ans *= 2
            ans %= MOD
        print(ans)


if __name__ == '__main__':
    main()
