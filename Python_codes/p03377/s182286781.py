#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    A, B, X = map(int, input().split())
    print('YES'if X - A >= 0 and B >= X - A else 'NO')


if __name__ == "__main__":
    main()
