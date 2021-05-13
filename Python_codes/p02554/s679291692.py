#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    mod = 10**9 + 7
    print((10**N - 9**N - 9**N + 8**N) % mod)


if __name__ == "__main__":
    main()
