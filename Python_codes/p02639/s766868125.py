import math
import sys
readline = sys.stdin.readline


def main():
    print(list(map(int, readline().rstrip().split())).index(0) + 1)


if __name__ == '__main__':
    main()
