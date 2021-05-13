#

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    w, h, x, y = input_int_list()
    area = (w * h) / 2
    bl = (w == 2 * x and h == 2 * y)
    print(area, 1 if bl else 0)
    return


if __name__ == "__main__":
    main()
