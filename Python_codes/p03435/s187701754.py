#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-26 20:10:47 +0900
# LastModified: 2020-06-26 20:35:09 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    c = []
    for _ in range(3):
        c.append(list(map(int, input().split())))
    a_12 = c[0][0]-c[1][0]
    a_13 = c[0][0]-c[2][0]
    a_23 = c[1][0]-c[2][0]
    b_12 = c[0][0]-c[0][1]
    b_13 = c[0][0]-c[0][2]
    b_23 = c[0][1]-c[0][2]

    for i in range(1, 3):
        if b_12 != c[i][0]-c[i][1] or b_13 != c[i][0]-c[i][2] or b_23 != c[i][1]-c[i][2]:
            print("No")
            return
        if a_12 != c[0][i]-c[1][i] or a_13 != c[0][i]-c[2][i] or a_23 != c[1][i]-c[2][i]:
            print("No")
            return
    print("Yes")



        


if __name__ == "__main__":
    main()
