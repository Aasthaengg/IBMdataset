import sys
from math import gcd
from functools import reduce

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def lcm(a, b):
    return a // gcd(a, b) * b


def main():
    N, *A = map(int, read().split())

    ans = 0
    l = 1
    for a in A:
        l, l_prev = lcm(l, a), l
        ans = (ans * (l // l_prev) % MOD + l // a) % MOD

    print(ans)
    return


if __name__ == '__main__':
    main()
