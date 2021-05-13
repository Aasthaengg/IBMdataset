#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-26 15:54:41 +0900
# LastModified: 2020-06-26 16:12:17 +0900
#


import copy
# import numpy as np
# import pandas as pd


def main():
    n, m = map(int, input().split())
    x_y = []
    goal = []
    for i in range(n):
        x_y.append(list(map(int, input().split())))
    for i in range(m):
        goal.append(list(map(int, input().split())))

    for xy in x_y:
        tmp = list(map(lambda x: abs(xy[0]-x[0])+abs(xy[1]-x[1]), goal))
        print(tmp.index(min(tmp))+1)



if __name__ == "__main__":
    main()
