import itertools
from collections import defaultdict


def main():
    N = int(input())
    if N == 1:
        print(1)

    else:
        XY = [list(map(int, input().split())) for _ in range(N)]

        dd = defaultdict(int)

        for xy1, xy2 in itertools.combinations(XY, 2):
            a = (xy2[0] - xy1[0], xy2[1] - xy1[1])
            b = (-a[0], -a[1])
            dd[a] += 1
            dd[b] += 1

        print(N - max(dd.values()))


main()
