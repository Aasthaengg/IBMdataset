import math
import sys


def parse(file):
    n, k = map(int, file.readline().split())
    return n, k


def main(n, k):
    if k % 2 == 1:
        return math.floor(n / k) ** 3
    else:
        return math.floor(n / k) ** 3 + math.floor((n + k/2) / k) ** 3


if __name__ == '__main__':
    print(main(*parse(sys.stdin)))