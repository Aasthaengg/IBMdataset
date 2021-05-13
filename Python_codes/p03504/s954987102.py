import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, c = map(int, readline().split())
    l = 2 * (10 ** 5) + 1
    cum = [0] * l
    used = [[False] * l for _ in range(c + 1)]

    for i in range(n):
        s, t, c = map(int, readline().split())
        if used[c][2 * s]:
            cum[2 * s] += 1
        else:
            cum[2 * s - 1] += 1
            used[c][2 * s] = True

        if used[c][2 * t]:
            cum[2 * t - 1] -= 1
        else:
            cum[2 * t] -= 1
            used[c][2 * t] = True

    ans = 0
    cur = 0
    for x in cum:
        cur += x
        ans = max(ans, cur)

    print(ans)


if __name__ == '__main__':
    main()
