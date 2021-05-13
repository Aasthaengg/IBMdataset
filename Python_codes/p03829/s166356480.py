import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, a, b = map(int, readline().split())
    x = list(map(int, readline().split()))

    l = (b + a - 1) // a
    ans = 0
    for i in range(n-1):
        diff = x[i + 1] - x[i]
        if diff >= l:
            ans += b
        else:
            ans += a * diff

    print(ans)


if __name__ == '__main__':
    main()
