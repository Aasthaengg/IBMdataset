import sys
import itertools
from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

in_n = lambda: int(readline())
in_nn = lambda: map(int, readline().split())
in_nl = lambda: list(map(int, readline().split()))
in_na = lambda: map(int, read().split())
in_s = lambda: readline().rstrip().decode('utf-8')


def main():
    N = in_n()
    xy = [tuple(in_nn()) for _ in range(N)]

    if N == 1:
        print(1)
        exit()

    comb = itertools.combinations(range(N), 2)
    d = defaultdict(int)

    for i, j in comb:
        x1, y1 = xy[i]
        x2, y2 = xy[j]
        xd = x2 - x1
        yd = y2 - y1
        d[(xd, yd)] += 1
        d[(-xd, -yd)] += 1

    ans = N - max(d.values())
    # print(d)
    print(ans)


if __name__ == '__main__':
    main()
