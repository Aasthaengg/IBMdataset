#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-08-30 14:36:32 +0900
# LastModified: 2020-08-30 14:45:15 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, a, b = map(int, input().split())
    tmp = n - n // (a+b) * (a+b)
    ans = n//(a+b) * a
    if tmp <= a:
        print(ans+tmp)
    else:
        print(ans+a)


if __name__ == "__main__":
    main()
