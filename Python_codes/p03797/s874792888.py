#!/usr/bin/env pytHon3
# -*- coding: utf-8 -*-


def main():
    N, M = map(int, input().split())

    if M - 2 * N > 0:
        x = (M - 2 * N) // 4
        print(N + x)
    else:
        print(M // 2)


if __name__ == "__main__":
    main()
