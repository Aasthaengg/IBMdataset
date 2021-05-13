import math
import sys


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(20000000)

MOD = 10 ** 9 + 7
INF = float("inf")


def main():
    X = int(input())
    a = math.gcd(X, 360)
    a = X * 360 // a
    print(a // X)


if __name__ == "__main__":
    main()
