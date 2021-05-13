import sys, os, math, bisect, itertools, collections, heapq, queue
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict

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

    N, K = il()
    cnt = defaultdict(int)
    for i in range(1, N + 1):
        cnt[i % K] += 1

    ret = 0
    for a in range(K):
        b = (K - a) % K
        c = (K - a) % K
        if (b + c) % K != 0: continue
        ret += cnt[a] * cnt[b] * cnt[c]
    print(ret)


if __name__ == '__main__':
    main()
