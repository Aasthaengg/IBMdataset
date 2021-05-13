#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-07-29 14:54:21 +0900
# LastModified: 2020-07-29 15:02:31 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from collections import Counter


def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    a_cnt = Counter(a)
    keys = a_cnt.keys()
    values = a_cnt.values()
    cnt = 0
    for k, v in zip(keys, values):
        if v % 2 == 1:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
