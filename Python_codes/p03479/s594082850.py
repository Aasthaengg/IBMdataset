#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-08-23 00:17:05 +0900
# LastModified: 2020-08-23 00:29:38 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    x, y = map(int, input().split())
    baibai = x
    cnt = 0
    while baibai <= y:
        cnt += 1
        baibai *= 2
    print(cnt)


if __name__ == "__main__":
    main()
