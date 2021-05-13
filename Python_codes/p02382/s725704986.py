# coding=utf-8
from math import sqrt


def main():
    d = input()
    x = map(int, raw_input().split())
    y = map(int, raw_input().split())
    z = [abs(x - y) for x, y in zip(x, y)]
    print sum(z)
    print sqrt(sum([w ** 2 for w in z]))
    print sum([w ** 3 for w in z]) ** (1.0 / 3)
    print max(z)


if __name__ == '__main__':
    main()