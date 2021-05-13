#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-26 19:48:52 +0900
# LastModified: 2020-06-26 20:06:44 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, t = map(int, input().split())
    time = list(map(int, input().split()))
    total = 0
    for i in range(0,n-1):
        cur = time[i]
        nex = time[i+1]
        if cur+t+1<=nex:
            total += t
        else:
            total += nex-cur
#        print(total)
    print(total+t)


if __name__ == "__main__":
    main()
