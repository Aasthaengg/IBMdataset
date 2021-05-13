import math


# def calc(n, c, d):
#     return n-(math.floor(n / c) +
#               math.floor(n / d) - math.floor(n / (c * d / math.gcd(c, d))))
def calc(n, c, d):
    return n-(n // c +
              n // d - n // (c * d // math.gcd(c, d)))


def main():
    a, b, c, d = map(int, input().split())

    print(calc(b, c, d)-calc(a-1, c, d))


if __name__ == "__main__":
    main()
