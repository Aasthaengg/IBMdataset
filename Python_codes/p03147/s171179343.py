#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix_2
# CreatedDate:  2020-07-30 18:19:19 +0900
# LastModified: 2020-07-30 18:49:07 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from itertools import groupby


def main():
    n = int(input())
    H = list(map(int, input().split()))
    A = []
    for i in range(max(H)+1):
        A.append([1 if h > i else 0 for h in H])

    cnt = 0
    for a in A:
        ans = groupby(a)
        for k, g in ans:
            if 1 in list(g):
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
