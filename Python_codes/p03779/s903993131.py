#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-07-31 13:48:14 +0900
# LastModified: 2020-07-31 14:24:21 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from math import sqrt


def main():
    X = abs(int(input()))
    s = (-1+sqrt(1+8*X))/2
    if s.is_integer():
        s = int(s)
    else:
        s = int(s) + 1
    print(s)



if __name__ == "__main__":
    main()
