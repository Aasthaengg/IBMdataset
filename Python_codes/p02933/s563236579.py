#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(inp):
    A = int(inp.readline().strip())
    S = inp.readline().strip()
    if A >= 3200:
        return S
    else:
        print("red")


def main():
    import sys
    result = solve(sys.stdin)
    if result is not None and result != '':
        print(result)


if __name__ == '__main__':
    main()
