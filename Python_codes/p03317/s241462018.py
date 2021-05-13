#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print((N + K - 3) // ~-K)


if __name__ == "__main__":
    main()
