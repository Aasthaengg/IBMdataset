#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 22:12:11 +0900
# LastModified: 2020-06-25 22:33:48 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    if x<a[0] or a[-1]<x:
        print("0")
        return

    for i in range(len(a)):
        if a[i] > x:
            tmp = i
            break
    if tmp < m-tmp:
        print(tmp)
    else:
        print(m-tmp)
            



if __name__ == "__main__":
    main()
