import sys

sys.setrecursionlimit(10000000)
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
    A = il()
    B = il()
    C = il()

    ret = 0
    for n in range(N):
        ret += B[A[n] - 1]
        if n > 0 and A[n] == A[n - 1] + 1:
            ret += C[A[n - 1]-1]
    print(ret)


if __name__ == '__main__':
    main()
