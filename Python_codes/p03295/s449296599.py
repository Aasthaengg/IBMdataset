import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import defaultdict

    n, m = map(int, readline().split())
    cum = [0] * n

    war = defaultdict(list)

    for _ in range(m):
        a, b = map(int, readline().split())
        war[a].append(b)

    ans = 0
    cur = n + 1
    for i in range(1, n + 1):
        if cur == i:
            ans += 1
            cur = n + 1
        ng = war[i]
        if ng:
            cur = min(cur, min(ng))

    print(ans)

if __name__ == '__main__':
    main()
