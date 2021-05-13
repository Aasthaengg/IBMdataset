import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque

# import fractions

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)
# lcm = lambda x, y: (x * y) // fractions.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def calcTwoPointDistance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    sx, sy, tx, ty = il()

    move = []
    for _ in range(sy, ty):
        move.append('U')
    for _ in range(sx, tx):
        move.append('R')
    for _ in range(sy, ty):
        move.append('D')
    for _ in range(sx, tx):
        move.append('L')
    move.append('L')

    for _ in range(sy, ty + 1):
        move.append('U')
    for _ in range(sx, tx + 1):
        move.append('R')
    move.append('D')
    move.append('R')
    for _ in range(sy, ty + 1):
        move.append('D')
    for _ in range(sx, tx + 1):
        move.append('L')
    move.append('U')

    print(*move, sep='')


if __name__ == '__main__':
    main()
