#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-27 10:45:46 +0900
# LastModified: 2020-06-27 11:10:23 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n = int(input())
    current = [0, 0, 0]
    flag = 0
    for _ in range(n):
        t, x, y = map(int, input().split())
        if flag == 1:
            continue
        judge = int(abs(x-current[1]))+int(abs(y-current[2]))
#        print(judge)
        if t-current[0] < judge:
            flag = 1
        elif t-current[0] == judge:
#            print(t,x,y)
            current[0] = t
            current[1] = x
            current[2] = y
        else:
            ama = t-current[0]
            if (ama-judge)%2 != 0:
                flag = 1
            else:
                current[0] = t
                current[1] = x
                current[2] = y

    if flag == 0:
        print("Yes")
    if flag == 1:
        print("No")



if __name__ == "__main__":
    main()
