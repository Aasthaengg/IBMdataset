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


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = il()

    cnt, q1 = 0, 0
    ism = False
    for a in A:
        cnt += a
        if ism and cnt >= 0:
            q1 += abs(cnt) + 1
            cnt = -1
        elif not ism and cnt <= 0:
            q1 += abs(cnt) + 1
            cnt = 1
        if ism:
            ism = False
        else:
            ism = True

    cnt , q2 = 0, 0
    ism = True
    for a in A:
        cnt += a
        if ism and cnt >= 0:
            q2 += abs(cnt) + 1
            cnt = -1
        elif not ism and cnt <= 0:
            q2 += abs(cnt) + 1
            cnt = 1
        if ism:
            ism = False
        else:
            ism = True
    print(min(q1,q2))


if __name__ == '__main__':
    main()
