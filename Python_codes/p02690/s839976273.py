#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D_fix
# CreatedDate:  2020-08-08 01:53:55 +0900
# LastModified: 2020-08-08 01:56:11 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    x = int(input())
    for a in range(-120, 120):
        for b in range(-120, a):
            if a**5-b**5 == x:
                print("{} {}".format(a, b))
                return


if __name__ == "__main__":
    main()
