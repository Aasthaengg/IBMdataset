import sys, os, math, bisect, itertools, collections, heapq, queue
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal

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
    S = iss()
    mx = S.count('R') * S.count('G') * S.count('B')

    for i in range(N):
        for j in range(i+1, N):
            k = j + j - i
            if k < N and S[i] != S[j] and S[i] != S[k] and S[j] != S[k]:
                mx -= 1
    print(mx)


if __name__ == '__main__':
    main()
