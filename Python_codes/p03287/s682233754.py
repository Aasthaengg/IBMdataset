import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter

    n, m = map(int, readline().split())
    a = list(map(int, readline().split()))

    counter = Counter()
    counter[0] = 1

    cur = 0
    for x in a:
        cur += x
        cur %= m
        counter[cur] += 1

    ans = 0
    for key, val in counter.items():
        ans += val * (val - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
