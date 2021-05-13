import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n = int(readline())
    t = list(map(int, readline().split()))
    a = list(map(int, readline().split()))

    r = [[1, 10 ** 9 + 1] for _ in range(n)]
    r[0][0], r[0][1] = t[0], t[0]

    for i, x in enumerate(t[1:], 1):
        if t[i - 1] < t[i]:
            r[i][0], r[i][1] = t[i], t[i]
        else:
            r[i][0], r[i][1] = 1, t[i]

    s = [[1, 10 ** 9 + 1] for _ in range(n)]
    a_rev = a[::-1]
    s[0][0], s[0][1] = a[0], a[0]

    for i, x in enumerate(a_rev[1:], 1):
        if a_rev[i - 1] < a_rev[i]:
            s[i][0], s[i][1] = a_rev[i], a_rev[i]
        else:
            s[i][0], s[i][1] = 1, a_rev[i]

    s = s[::-1]
    ans = 1

    for i in range(n):
        lower = max(r[i][0], s[i][0])
        upper = min(r[i][1], s[i][1])
        d = max(upper - lower + 1, 0)
        ans *= d
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
