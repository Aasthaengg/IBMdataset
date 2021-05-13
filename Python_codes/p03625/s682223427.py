#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter


def main():
    N = int(input())
    A = list(map(int, input().split()))

    count = Counter(A)
    count = sorted(count.items(), key=lambda x: (-x[0], x[1]))
    count = [(k, v) for k, v in count if v >= 2]
    if len(count) < 2:
        print(0)
    elif count[0][1] >= 4:
        print(count[0][0] ** 2)
    else:
        print(count[0][0] * count[1][0])


if __name__ == "__main__":
    main()
