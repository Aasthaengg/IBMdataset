#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    T, A = 1, 1

    for i in range(N):
        t, a = map(int, input().split())
        m = max((T + t - 1) // t, (A + a - 1) // a)
        T, A = t * m, a * m
    print(T + A)


if __name__ == "__main__":
    main()
