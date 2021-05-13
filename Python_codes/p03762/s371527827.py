from collections import defaultdict, Counter
from itertools import product, groupby, count, permutations, combinations
from math import pi, sqrt
from collections import deque
from bisect import bisect, bisect_left, bisect_right
from string import ascii_lowercase
from functools import lru_cache
import sys
sys.setrecursionlimit(10000)
INF = float("inf")
YES, Yes, yes, NO, No, no = "YES", "Yes", "yes", "NO", "No", "no"
dy4, dx4 = [0, 1, 0, -1], [1, 0, -1, 0]
dy8, dx8 = [0, -1, 0, 1, 1, -1, -1, 1], [1, 0, -1, 0, 1, 1, -1, -1]


def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W


def ceil(a, b):
    return (a + b - 1) // b


def main():
    n, m = map(int, input().split())
    x_list = list(sorted(list(map(int, input().split()))))
    y_list = list(sorted(list(map(int, input().split()))))
    MOD = 10 ** 9 + 7

    x = 0
    for i, d in enumerate(range(-(n - 1), n, 2)):
        x += d * x_list[i]
        x %= MOD

    y = 0
    for i, d in enumerate(range(-(m - 1), m, 2)):
        y += d * y_list[i]
        y %= MOD
        
    print((x * y) % MOD)




if __name__ == '__main__':
    main()
