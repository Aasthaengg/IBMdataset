#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    X = int(input())

    result = (X // 11) * 2
    X %= 11

    if X == 0:
        print(result)
    elif X <= 6:
        print(result + 1)
    else:
        print(result + 2)


if __name__ == "__main__":
    main()
