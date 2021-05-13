#!/usr/bin/env python
# -*- coding: utf-8 -*-


def mygcd(x, y):
    if x == 0 or y == 0:
        return max(x, y)
    else:
        (x1, y1) = (max(x, y), min(x, y))
        return mygcd(y, x % y)


def main():
    print(mygcd(*map(int, input().split())))

if __name__ == "__main__":
    main()