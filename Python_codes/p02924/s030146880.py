#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solve(inp):
    N = int(inp.readline().strip())

    r = (N * (N - 1)) // 2
    return int(r)


def main():
    import sys
    result = solve(sys.stdin)
    if result is not None and result != '':
        print(result)


if __name__ == '__main__':
    main()
