#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-08-18 14:31:47 +0900
# LastModified: 2020-08-18 14:42:13 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    ans_box = dict()
    for _ in range(n):
        s = sorted(map(str, input()))
        if ''.join(s) in ans_box.keys():
            ans_box[''.join(s)] += 1
        else:
            ans_box[''.join(s)] = 1
    ans = 0
    for key, value in ans_box.items():
        if value == 1:
            pass
        else:
            ans += value*(value-1)//2
    print(ans)

if __name__ == "__main__":
    main()
