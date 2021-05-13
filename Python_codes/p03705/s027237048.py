#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	A
# CreatedDate:  2020-07-29 16:51:04 +0900
# LastModified: 2020-07-29 16:59:15 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, a, b = map(int, input().split())
    down = (n-1)*a + b
    up = (n-1)*b + a
    if up-down+1 > 0:
        print(up-down+1)
    else:
        print(0)


if __name__ == "__main__":
    main()
