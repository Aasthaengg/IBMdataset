#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-26 15:04:28 +0900
# LastModified: 2020-06-26 15:10:43 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    a, b, c = map(int, input().split())
    for i in range(100):
        if float((a*i-c)/b).is_integer():
            print("YES")
            return
    print("NO")



if __name__ == "__main__":
    main()
