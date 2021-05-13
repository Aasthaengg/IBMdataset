#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    A, B, C, D = map(int, input().split())
    ans = -10**9**2

    for ab in (A, B):
        for cd in (C, D):
            if ab * cd > ans:
                ans = ab * cd

    print(ans)


if __name__ == "__main__":
    main()
