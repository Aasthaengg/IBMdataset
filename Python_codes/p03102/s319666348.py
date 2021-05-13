#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 13:57:00 +0900
# LastModified: 2020-06-25 14:12:29 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    count = 0
    for _ in range(n):
        a = list(map(int, input().split()))
        total = sum(a[i]*b[i] for i in range(m))+c
        if total>0:
            count+=1
    print(count)


if __name__ == "__main__":
    main()
