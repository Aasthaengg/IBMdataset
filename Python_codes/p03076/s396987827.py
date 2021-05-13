import sys
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    W = [a, b, c, d, e]

    d = 0
    p = []

    for i in range(5):
        x, y = divmod(W[i], 10)
        if y == 0:
            d += x
            p.append(10)
        else:
            d += x + 1
            p.append(y)

    print(d * 10 + min(p)-10)


if __name__ == "__main__":
    main()
