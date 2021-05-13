#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0

    for i in range(N):
        if (i + 1) % 2 != 0 and A[i] % 2 != 0:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
