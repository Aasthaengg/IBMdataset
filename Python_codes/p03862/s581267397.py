import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, x = map(int, readline().split())
    a = list(map(int, readline().split()))

    ans = 0

    for i in range(n - 1):
        diff = (a[i] + a[i + 1]) - x
        if diff > 0:
            ans += diff
            if diff > a[i + 1]:
                a[i] = a[i] - (diff - a[i + 1])
                a[i + 1] = 0
            else:
                a[i + 1] = a[i + 1] - diff

    print(ans)


if __name__ == '__main__':
    main()
