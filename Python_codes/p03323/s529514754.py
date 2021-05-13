#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B = map(int, input().split())
    print('Yay!'if A <= 8 and B <= 8 else ':(')


if __name__ == "__main__":
    main()
