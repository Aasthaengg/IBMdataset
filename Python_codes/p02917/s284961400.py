#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-04 13:28:04 +0900
# LastModified: 2020-09-04 13:47:38 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    b = list(map(int, input().split()))
    if n == 1:
        print(b[0]*2)
        return
    a = [-float('inf')]*n
    a[0] = b[0]
    a[1] = b[0]
    for i in range(1, n-1):
        if a[i] > b[i]:
            a[i] = b[i]
        a[i+1] = b[i]
    print(sum(a))



if __name__ == "__main__":
    main()
