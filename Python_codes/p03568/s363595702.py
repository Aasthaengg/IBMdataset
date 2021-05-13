#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-09-26 23:51:48 +0900
# LastModified: 2020-09-26 23:59:21 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd = 1
    for a in A:
        if a % 2 == 0:
            odd *= 2
        else:
            odd *= 1
    print(3**N-odd)

    



if __name__ == "__main__":
    main()
