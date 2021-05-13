from fractions import gcd
from functools import reduce


def main():
    balls, target = map(int, input().split())
    numbers = [int(x) for x in input().split()]
    numbers.sort()
    numbers_gcd = reduce(gcd, numbers)
    print("POSSIBLE" if target % numbers_gcd == 0 and target <= numbers[-1] else "IMPOSSIBLE")


if __name__ == '__main__':
    main()

