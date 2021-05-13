import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, x = map(int, readline().split())
    a = list(map(int, readline().split()))
    a.sort()

    rem = x
    ans = 0

    for i in range(n - 1):
        if rem >= a[i]:
            rem -= a[i]
            ans += 1

    if a[n-1] == rem:
        ans += 1

    print(ans)


if __name__ == '__main__':
    main()
