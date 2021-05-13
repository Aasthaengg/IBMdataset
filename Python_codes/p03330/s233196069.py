import sys
import math
import collections
import bisect
import copy
import itertools

# import numpy as np

sys.setrecursionlimit(10 ** 7)
INF = 10 ** 16
MOD = 10 ** 9 + 7
# MOD = 998244353

ni = lambda: int(sys.stdin.readline())
ns = lambda: map(int, sys.stdin.readline().split())
na = lambda: list(map(int, sys.stdin.readline().split()))
na1 = lambda: list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))


# ===CODE===


def main():
    n, c = ns()
    d = [na() for _ in range(c)]
    color = [na() for _ in range(n)]

    cnt = [[0] * c for _ in range(3)]

    for i in range(n):
        for j in range(n):
            cnt[(i + j) % 3][color[i][j] - 1] += 1

    ans = INF
    for cost in itertools.permutations(range(c), 3):
        tmp_ans = 0
        for i in range(3):
            for j in range(c):
                tmp_ans += cnt[i][j] * d[j][cost[i]]
        ans = min(ans, tmp_ans)

    print(ans)


if __name__ == '__main__':
    main()
