#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = list(map(int, input().split()))
    print(max(A) - min(A))


if __name__ == "__main__":
    main()
