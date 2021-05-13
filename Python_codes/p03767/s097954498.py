#!/usr/bin/env python3


def main():
    N, *A = map(int, open(0).read().split())
    A.sort()
    print(sum(A[-2 : -2 * N - 1 : -2]))


main()
