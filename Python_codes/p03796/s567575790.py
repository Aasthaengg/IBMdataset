import math


def answer(n: int) -> int:
    return math.factorial(n) % (10 ** 9 + 7)


def main():
    n = int(input())
    print(answer(n))

if __name__ == '__main__':
    main()
