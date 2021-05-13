import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter
    n, c = map(int, readline().split())
    cost = [list(map(int, readline().split())) for _ in range(c)]
    color = [list(map(int, readline().split())) for _ in range(n)]

    group = [Counter() for _ in range(3)]

    for i in range(n):
        for j in range(n):
            cur = (i + j) % 3
            group[cur][color[i][j]] += 1

    from itertools import permutations

    ans = INF

    for after in permutations(range(1, c + 1), 3):
        score = 0
        for gn, counter in enumerate(group):
            for key, val in counter.items():
                score += val * cost[key - 1][after[gn] - 1]
        ans = min(score, ans)

    print(ans)


if __name__ == '__main__':
    main()
