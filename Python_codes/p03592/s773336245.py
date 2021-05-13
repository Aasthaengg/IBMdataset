#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-07-26 12:46:01 +0900
# LastModified: 2020-07-26 13:19:34 +0900
#


import os
import sys


def main():
    n, m, k = map(int, input().split())
    for s in range(m+1):
        for t in range(n+1):
            if k == n*s+m*t-2*s*t:
                print("Yes")
                return
    print("No")


if __name__ == "__main__":
    main()
