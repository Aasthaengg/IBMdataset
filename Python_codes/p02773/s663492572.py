import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter

    N = int(readline())
    c = Counter()

    for _ in range(N):
        s = input()
        c[s] += 1

    _, cnt = c.most_common(1)[0]

    res = []
    for key, val in c.items():
        if val == cnt:
            res.append(key)

    res.sort()

    for x in res:
        print(x)


if __name__ == '__main__':
    main()
