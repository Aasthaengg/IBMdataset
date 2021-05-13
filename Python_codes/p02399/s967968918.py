#!usr/bin/env python3

from math import floor


def string_two_numbers_spliter():
    a, b = [int(i) for i in input().split()]
    return a, b


def main():
    a, b = string_two_numbers_spliter()
    print('%d %d %f' % (floor(a/b), a%b, a/b))


if __name__ == '__main__':
    main()