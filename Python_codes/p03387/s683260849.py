#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-09-26 23:35:00 +0900
# LastModified: 2020-09-26 23:50:15 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    L = list(map(int, input().split()))
    ans = 0
    max_idx = L.index(max(L))
    min_idx = L.index(min(L))
    for i in range(len(L)):
        if i == max_idx or i == min_idx:
            pass
        else:
            medium_idx = i
    ans += (L[max_idx] - L[medium_idx])
    L[medium_idx] = L[max_idx]
    L[min_idx] += ans
    if (L[max_idx]-L[min_idx]) % 2 == 0:
        print(ans + (L[max_idx]-L[min_idx])//2)
    else:
        print(ans + (L[max_idx]-L[min_idx]+1)//2 + 1)


if __name__ == "__main__":
    main()
