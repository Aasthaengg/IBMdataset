#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    A, B, C = map(int, input().split())
    K = int(input())

    for _ in range(K):
        if not A < B:
            B *= 2
        elif not B < C:
            C *= 2
    if A < B < C:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
