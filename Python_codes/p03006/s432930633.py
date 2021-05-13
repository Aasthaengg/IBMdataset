import sys
input = sys.stdin.readline
from collections import defaultdict


def read():
    N = int(input().strip())
    XY = []
    for i in range(N):
        x, y = map(int, input().strip().split())
        XY.append((x, y))
    return N, XY


def solve(N, XY):
    if N == 1:
        return 1

    min_cost = 1000000
    for j in range(N):
        for i in range(j):
            rdict = defaultdict(list)
            x0, y0 = XY[i]
            x1, y1 = XY[j]
            p, q = x1 - x0, y1 - y0
            for k in range(N):
                x, y = XY[k]
                rdict[q * x - p * y].append((x, y))
            cost = 0
            for v in rdict.values():
                vs = list(sorted(v))
                x0, y0 = vs[0]
                for x1, y1 in vs:
                    if x1 - x0 != p or y1 - y0 != q:
                        cost += 1
                    x0, y0 = x1, y1
            min_cost = min(min_cost, cost)
    return min_cost


if __name__ == '__main__':
    inputs = read()
    print(solve(*inputs))
