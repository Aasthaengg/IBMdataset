#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-25 17:30:38 +0900
# LastModified: 2020-06-25 21:19:30 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    while len(v) != 1:
        s = v.pop()
        t = v.pop()
        v.append((s+t)/2)
    print(v[0])


if __name__ == "__main__":
    main()
