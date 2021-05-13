# https://atcoder.jp/contests/agc038/tasks/agc038_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    h, w, a, b = input_int_list()
    grid = []
    for i in range(h):
        if i < b:
            grid.append("1" * a + "0" * (w - a))
        else:
            grid.append("0" * a + "1" * (w - a))
    for line in grid:
        print(line)

    return


if __name__ == "__main__":
    main()
