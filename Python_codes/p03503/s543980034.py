import sys
import os
import math
import bisect
import collections
import itertools
import heapq
import re
import queue

# import fractions

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
    F = [il() for _ in range(N)]
    P = [il() for _ in range(N)]

    ret = -MAX
    for b in range(1, 1 << 10):
        tmp = 0
        for n in range(N):
            o = 0
            for t in range(10):
                if b >> t & 1 and F[n][t] == 1:
                    o += 1
            tmp += P[n][o]
        ret = max(ret, tmp)
    print(ret)


if __name__ == '__main__':
    main()
