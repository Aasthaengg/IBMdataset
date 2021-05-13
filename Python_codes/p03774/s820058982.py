import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def f(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N, M = il()
    AB = [il() for _ in range(N)]
    CD = [il() for _ in range(M)]
    for a, b in AB:
        ret = MAX
        dist = MAX
        for m in range(M):
            c, d = CD[m]
            d = f(a, c, b, d)
            if d == dist:
                ret = min(m + 1, ret)
            elif d < dist:
                dist = d
                ret = m + 1
        print(ret)


if __name__ == '__main__':
    main()
