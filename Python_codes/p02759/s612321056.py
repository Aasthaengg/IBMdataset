import sys
from math import ceil


def main():
    input = sys.stdin.buffer.readline
    n = int(input())
    print(ceil(n / 2))


if __name__ == "__main__":
    main()
