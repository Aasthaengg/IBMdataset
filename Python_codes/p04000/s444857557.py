import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict
    h, w, n = map(int, readline().split())
    c = defaultdict(int)
    count = [0] * 10
    count[0] = (h - 2) * (w - 2)

    for _ in range(n):
        a, b = map(int, readline().split())
        a, b = a - 1, b - 1
        for row in range(max(2, a), min(h - 1, a + 2) + 1):
            for col in range(max(2, b), min(w - 1, b + 2) + 1):
                cur = c[(row, col)]
                count[cur] -= 1
                count[cur + 1] += 1
                c[(row, col)] += 1

    print(*count, sep="\n")


if __name__ == '__main__':
    main()
