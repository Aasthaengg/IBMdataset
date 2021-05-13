#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-25 17:21:17 +0900
# LastModified: 2020-06-25 17:28:09 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
#    print(d)
    if len(d)%2 == 1:
        print(0)
        return
    l = d[len(d)//2-1]
    r = d[len(d)//2]
    if l == r:
        print(0)
        return
    print(r-l)



if __name__ == "__main__":
    main()
