import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
import math
from collections import Counter


def read():
    S = int(input().strip())
    return S,


def solve(S):
    C = 10**9
    p, q = divmod(S, 10**9)
    if q == 0:
        ans = 0, 0, 0, p, 10**9, 1
    else:
        ans = 0, 0, 10**9-q, p+1, 10**9, 1
    print(*ans)


if __name__ == '__main__':
    inputs = read()
    solve(*inputs)
