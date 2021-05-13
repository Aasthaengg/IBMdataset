#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C_fix
# CreatedDate:  2020-08-08 21:55:54 +0900
# LastModified: 2020-08-08 22:01:55 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from itertools import permutations


def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    permu = list(map(list, permutations(range(1, n+1))))
    for index, per in enumerate(permu):
        if per == p:
            a = index
        if per == q:
            b = index
    print(abs(a-b))


if __name__ == "__main__":
    main()
