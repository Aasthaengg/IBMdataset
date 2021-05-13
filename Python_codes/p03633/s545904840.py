from math import gcd
from functools import reduce


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    n = int(input())
    t = {int(input()) for _ in range(n)}
    print(reduce(lcm, t))


if __name__ == '__main__':
    main()
