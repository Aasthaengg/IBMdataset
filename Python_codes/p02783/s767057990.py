import sys
from math import ceil


def main():
    input = sys.stdin.buffer.readline
    h, a = map(int, input().split())
    print(ceil(h / a))


if __name__ == "__main__":
    main()
