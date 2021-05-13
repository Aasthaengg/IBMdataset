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


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    N = ii()
    A = il()

    # 偶数番目の合計を負
    # 奇数番目の合計を正にするパターン
    sm, r1 = 0, 0
    for n in range(N):
        sm += A[n]
        if n % 2 == 0 and sm < 1:
            r1 += abs(sm) + 1
            sm = 1
        elif n % 2 != 0 and sm > -1:
            r1 += abs(sm) + 1
            sm = -1

    # 偶数番目の合計を正
    # 奇数番目の合計を負にするパターン
    sm, r2 = 0, 0
    for n in range(N):
        sm += A[n]
        if n % 2 == 0 and sm > -1:
            r2 += abs(sm) + 1
            sm = -1
        elif n % 2 != 0 and sm < 1:
            r2 += abs(sm) + 1
            sm = 1

    # 操作数が小さいほうを出力
    print(min(r1, r2))


if __name__ == '__main__':
    main()
