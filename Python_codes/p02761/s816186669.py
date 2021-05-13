#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix_2
# CreatedDate:  2020-07-29 15:34:23 +0900
# LastModified: 2020-07-29 15:51:13 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m = map(int, input().split())
    num = [None] * (n+1)
    for _ in range(m):
        s, c = map(int, input().split())
        if (num[s] is not None and num[s] != c) or (s == 1 and c == 0 and len(num)>2):
            print(-1)
            return
        num[s] = c
    num = [0 if x is None else x for x in num]
    for i in range(1, n+1):
        if num[i] == 0 and i == 1 and len(num) > 2:
            print("1", end="")
            continue
        elif i == 1 and num[i] == 0 and len(num) == 2:
            print(0)
            return
        print("{}".format(num[i]), end="")
    print()

if __name__ == "__main__":
    main()
