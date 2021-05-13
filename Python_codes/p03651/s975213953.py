import sys
from math import gcd

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    if k > max(A):
        print("IMPOSSIBLE")
        exit()

    g = A[0]
    for a in A:
        g = gcd(g, a)

    print("POSSIBLE" if k % g == 0 else "IMPOSSIBLE")


if __name__ == '__main__':
    resolve()
