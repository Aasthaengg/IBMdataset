import math


def main():
    A, B, C, D = map(int, input().split())

    Takeshi = math.ceil(C/B)
    Aoki = math.ceil(A/D)

    print('Yes' if Takeshi<= Aoki else 'No')


if __name__ == '__main__':
    main()