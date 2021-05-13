#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    X, A, B = map(int, input().split())
    print('A'if abs(X - A) < abs(X - B)else 'B')


if __name__ == "__main__":
    main()
