#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    X, A, B = map(int, input().split())
    if B - A > X:
        print('dangerous')
    elif 0 < B - A <= X:
        print('safe')
    else:
        print('delicious')


if __name__ == "__main__":
    main()
