#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D
# CreatedDate:  2020-08-30 14:25:42 +0900
# LastModified: 2020-08-30 14:34:10 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    if not 1 in A:
        print(-1)
        return
    index = 0
    for a in A:
        if index+1 == a:
            index += 1
    print(N-index)


if __name__ == "__main__":
    main()
