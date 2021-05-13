#!usr/bin/env python3

import sys


def reverse_list():
    lst = [int(i) for i in sys.stdin.readline().split()]
    lst.reverse()
    return lst


def main():
    n = sys.stdin.readline()
    print(*reverse_list())


if __name__ == '__main__':
    main()