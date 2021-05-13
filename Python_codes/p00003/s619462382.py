#!/usr/bin/env python
# coding: utf-8


def is_right_triangle(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def main():
    input_count = int(raw_input())
    for i in xrange(input_count):
        L = raw_input().split(" ")
        L = map(long, L)
        L.sort()
        print ("NO", "YES")[is_right_triangle(*L)]

if __name__ == '__main__':
    main()