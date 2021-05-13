from math import gcd
from functools import reduce


def main():
    _ = int(input())
    a = list(map(int, input().split()))
    mod = 10 ** 9 + 7

    def lcm(x, y):
        return x * y // gcd(x, y)

    a_lcm = reduce(lcm, a)
    print(sum([a_lcm * pow(aa, mod - 2, mod) % mod for aa in a]) % mod)


if __name__ == '__main__':
    main()
