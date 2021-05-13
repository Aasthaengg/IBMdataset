import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from itertools import accumulate

    n, k = map(int, readline().split())
    item = [[] for _ in range(4)]
    cnt = [0] * 4

    w, v = map(int, readline().split())
    first = w
    item[0].append(v)
    cnt[0] += 1

    for i in range(n - 1):
        w, v = map(int, readline().split())
        item[w - first].append(v)
        cnt[w - first] += 1

    for i in range(4):
        item[i].sort(reverse=True)

    acc = [[0] + list(accumulate(item[i])) for i in range(4)]

    ans = 0
    for p in range(cnt[0] + 1):
        for q in range(cnt[1] + 1):
            for r in range(cnt[2] + 1):
                for s in range(cnt[3] + 1):
                    weight = (p + q + r + s) * first + q + 2 * r + 3 * s
                    if weight > k:
                        break
                    value = acc[0][p] + acc[1][q] + acc[2][r] + acc[3][s]
                    ans = max(ans, value)

    print(ans)


if __name__ == '__main__':
    main()
