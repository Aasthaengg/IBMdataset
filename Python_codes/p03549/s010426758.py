# https://atcoder.jp/contests/abc078/tasks/arc085_a

import sys
# sys.setrecursionlimit(100000)


def input():
    return sys.stdin.readline().strip()


def input_int():
    return int(input())


def input_int_list():
    return [int(i) for i in input().split()]


def main():
    n, m = input_int_list()
    ans = (1900 * m + 100 * (n - m)) * 2**m
    print(ans)

    return


if __name__ == "__main__":
    main()
