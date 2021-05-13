import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, k = map(int, readline().split())
    ans = 0

    for x in range(1, n + 1):
        p = n // x
        q = n % x
        ans += p * max(0, x - k)
        if k == 0:
            ans += q
        else:
            ans += max(0, q - k + 1)
    print(ans)


if __name__ == '__main__':
    main()
