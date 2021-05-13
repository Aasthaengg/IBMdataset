from collections import defaultdict
from itertools import product, groupby
from math import pi
from collections import deque
from bisect import bisect, bisect_left, bisect_right
INF = 10 ** 10


def main():
    n, m = map(int, input().split())
    print((n - 1) * (m - 1))


if __name__ == '__main__':
    main()
