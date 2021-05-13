#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 15:01:19 +0900
# LastModified: 2020-06-25 15:40:42 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    s = input()
    while s:
        s = s[:-1]
        if len(s)%2!=0:
            continue
        mid = len(s)//2
        left = s[:mid]
        right = s[mid:]
        if left==right:
            print(len(s))
            return

    


if __name__ == "__main__":
    main()
