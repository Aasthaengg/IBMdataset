import math


def main():
    N = int(input())
    power = math.factorial(N)
    print(power % (10 ** 9 + 7))


if __name__ == "__main__":
    main()
