import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, m, c = map(int, readline().split())
    b = list(map(int, readline().split()))

    ans = 0

    for i in range(n):
        a = list(map(int, readline().split()))
        cur = c
        for j in range(m):
            cur += a[j] * b[j]
        if cur > 0:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
