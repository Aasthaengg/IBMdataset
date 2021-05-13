#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-08-22 13:23:10 +0900
# LastModified: 2020-08-22 13:37:55 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m = map(int, input().split())
    stairs = [0]*(n+1)
    stairs[0] = 1
    for _ in range(m):
        a = int(input())
        stairs[a] = -1
    for i in range(n-1):
        if stairs[i] == -1:
            continue

        if stairs[i+1] == -1:
            pass
        else:
            stairs[i+1] += stairs[i]

        if stairs[i+2] == -1:
            pass
        else:
            stairs[i+2] += stairs[i]
    if stairs[n-1] != -1:
        print((stairs[n-1]+stairs[n])%1000000007)
    else:
        print(stairs[n]%1000000007)


if __name__ == "__main__":
    main()
