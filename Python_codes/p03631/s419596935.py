#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = list(input())
    print('Yes'if N[::1] == N[::-1] else 'No')


if __name__ == "__main__":
    main()
