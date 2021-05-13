import math


def main(n, a, b):
    def validator(x, a, b):
        total = sum([(x // (10 ** digit)) %
                     10 for digit in range(int(math.log10(n)) + 1)])
        return total >= a and total <= b
    print(sum([x for x in range(1, n + 1) if validator(x, a, b)]))


if __name__ == "__main__":
    n, a, b = [int(x) for x in input().split()]
    main(n, a, b)
