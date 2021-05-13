import sys
from math import ceil


def main():
    input = sys.stdin.buffer.readline
    a, b = map(int, input().split())
    print(ceil((b - 1) / (a - 1)))


if __name__ == "__main__":
    main()
