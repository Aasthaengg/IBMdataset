#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, C, D = map(int, input().split())
    print('Yes'if (	abs(A - B) <= D and abs(B - C) <= D)
          or abs(A - C) <= D else 'No')


if __name__ == "__main__":
    main()
