import sys
from math import gcd

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def lcm(a, b):
    return a * b // gcd(a, b)


def main():
    N, *T = map(int, read().split())

    ans = 1
    for t in T:
        ans = lcm(ans, t)

    print(ans)
    return


if __name__ == '__main__':
    main()
