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

    H, W = il()
    S = [iss() for _ in range(H)]

    move = [[-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]
    ret = []
    for _ in range(H):
        ret.append([0] * W)

    for h in range(H):
        for w in range(W):
            if S[h][w] == '.':
                continue
            else:
                ret[h][w] = '#'
                for mw, mh in move:
                    if w + mw >= W or h + mh >= H: continue
                    if w + mw < 0 or h + mh < 0: continue
                    if ret[h + mh][w + mw] != '#': ret[h + mh][w + mw] += 1

    for r in ret:
        print(*r, sep='')


if __name__ == '__main__':
    main()
