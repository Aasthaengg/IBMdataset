#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 16:13:15 +0900
# LastModified: 2020-06-25 16:26:22 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    s = input()
    total = 0
    for i in range(1,n):
        cnt = 0
        left = s[:i]
        right = s[i:]
        left = list(set(left))
        right = list(set(right))
        for l in left:
            if l in right:
                cnt += 1
        if total < cnt:
            total = cnt
    print(total)


if __name__ == "__main__":
    main()
