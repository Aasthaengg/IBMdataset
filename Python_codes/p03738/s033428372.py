#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-07-17 12:17:41 +0900
# LastModified: 2020-07-17 12:18:40 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    a = int(input())
    b = int(input())
    if a>b:
        print("GREATER")
    elif a==b:
        print("EQUAL")
    else:
        print("LESS")


if __name__ == "__main__":
    main()
