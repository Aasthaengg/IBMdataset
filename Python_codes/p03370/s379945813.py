#!/usr/bin/env python3


def main():
    N, X, *M = map(int, open(0).read().split())
    print(N + ((X - sum(M)) // min(M)))


main()
