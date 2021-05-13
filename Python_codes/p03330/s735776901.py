# ABC099D - Good Grid
import sys
input = sys.stdin.readline

from collections import Counter
from itertools import product


def main():
    N, C = map(int, input().split())
    D = [0] + list([0] + list(map(int, input().split())) for _ in range(C))
    grid = tuple(tuple(map(int, input().split())) for _ in range(N))
    cost = [Counter() for _ in range(3)]
    for i, g in enumerate(grid):  # classify each cell by mod3
        for j in range(3):
            cost[(i + j) % 3].update(g[j::3])
    dist = [[] for _ in range(3)]
    # compute the actual cost to change color
    for i, tgt in product(range(3), range(1, C + 1)):
        cur = sum(D[src][tgt] * cnt for src, cnt in cost[i].items())
        dist[i].append(cur)
    ans = 1 << 60
    # fix two colors and compute the minimum cost
    for i, j in product(range(C), repeat=2):
        if i == j:
            continue
        cur = dist[0][i] + dist[1][j]
        cur += min(x for k, x in enumerate(dist[2]) if k not in (i, j))
        ans = min(ans, cur)
    print(ans)


if __name__ == "__main__":
    main()