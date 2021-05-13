import math
from functools import reduce


def gcd(*numbers):  # greatest common divisor
    return reduce(math.gcd, numbers)


def lcm_base(x, y):  # least common multiplier
    return (x*y) // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def main():
    n = int(input())
    t = []
    for i in range(n):
        t.append(int(input()))

    answer = lcm(*t)

    print(answer)


if __name__ == "__main__":
    main()
