#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
input = sys.stdin.readline


def main():
    a, b, c = map(int, input().split())

    if a <= c and c <= b:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
