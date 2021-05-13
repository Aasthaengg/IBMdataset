import math
import sys
readline = sys.stdin.readline


def main():
    s, w = map(int, readline().rstrip().split())
    print("unsafe" if s <= w else "safe")


if __name__ == '__main__':
    main()
