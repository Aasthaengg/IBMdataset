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

    A, B, Q = il()
    S = [-MAX, MAX]
    for _ in range(A):
        S.append(ii())
    S.sort()
    T = [-MAX, MAX]
    for _ in range(B):
        T.append(ii())
    T.sort()

    for _ in range(Q):
        q = ii()
        Srange = bisect.bisect_left(S, q)
        Trange = bisect.bisect_left(T, q)
        print(min(abs(q - S[Srange - 1]) + abs(S[Srange - 1] - T[Trange]),
                  abs(q - S[Srange - 1]) + abs(S[Srange - 1] - T[Trange - 1]),
                  abs(q - S[Srange]) + abs(S[Srange] - T[Trange - 1]),
                  abs(q - S[Srange]) + abs(S[Srange] - T[Trange]),
                  abs(q - T[Trange - 1]) + abs(T[Trange - 1] - S[Srange]),
                  abs(q - T[Trange - 1]) + abs(T[Trange - 1] - S[Srange - 1]),
                  abs(q - T[Trange]) + abs(T[Trange] - S[Srange - 1]),
                  abs(q - T[Trange]) + abs(T[Trange] - S[Srange])))


if __name__ == '__main__':
    main()
