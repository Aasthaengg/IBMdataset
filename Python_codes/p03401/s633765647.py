#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    S = sum(abs(A[i] - A[i - 1]) for i in range(1, N + 2))

    for i in range(1, N + 1):
        l, r = min(A[i - 1], A[i + 1]), max(A[i - 1], A[i + 1])
        if l <= A[i] <= r:
            print(S)
        elif A[i] <= l:
            print(S - 2 * (l - A[i]))
        else:
            print(S - 2 * (A[i] - r))


if __name__ == "__main__":
    main()
