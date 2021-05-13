from collections import Counter
import sys
from functools import lru_cache
from functools import reduce
from operator import mul
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


@lru_cache(None)
def cmb(n: int, r: int):
    if n < r:
        return 0
    r = min(n - r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def main():
    _ = int(input().strip())
    A = [int(i) for i in input().strip().split()]
    cnts = Counter(A)
    d = {}
    _sum = 0
    for k, v in cnts.items():
        d[k] = (cmb(v, 2), cmb(v - 1, 2))
        _sum += d[k][0]
    for a in A:
        dif = d[a][0] - d[a][1]
        print(_sum - dif)
    return


if __name__ == "__main__":
    main()
