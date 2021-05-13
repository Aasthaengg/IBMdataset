import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate

    n = int(input())
    a = list(map(int, readline().split()))
    a_cum = [0] * (n + 1)
    a_cum[n] = a[n]

    for i in range(n - 1, -1, -1):
        a_cum[i] = a_cum[i + 1] + a[i]

    b = [0] * (n + 1)
    b[0] = 1

    for i in range(n):
        b[i + 1] = min((b[i] - a[i]) * 2, a_cum[i + 1])

    ans = 0
    for i in range(n + 1):
        if b[i] < a[i]:
            print(-1)
            sys.exit()
        ans += b[i]

    print(ans)


if __name__ == '__main__':
    main()
