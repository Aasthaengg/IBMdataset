#!/usr/bin/env python3.8.3
# -*- coding: utf-8 -*-


def main():
    X = int(input())
    if X < 600:
        ans = 8
    elif X < 800:
        ans = 7
    elif X < 1000:
        ans = 6
    elif X < 1200:
        ans = 5
    elif X < 1400:
        ans = 4
    elif X < 1600:
        ans = 3
    elif X < 1800:
        ans = 2
    else:
        ans = 1

    print(ans)


if __name__ == "__main__":
    main()
