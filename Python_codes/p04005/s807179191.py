#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	A
# CreatedDate:  2020-09-27 00:18:14 +0900
# LastModified: 2020-09-27 00:27:44 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    A, B, C = map(int, input().split())
    abc = {
            "AB": [A*B, C],
            "AC": [A*C, B],
            "BC": [B*C, A]
          }
    max_value = 1e18
    for key, value in abc.items():
        if value[0] < max_value:
            important_key = key
            max_value = value[0]
    if abc[important_key][1] % 2 == 0:
        print(0)
    else:
        print(abc[important_key][0])


if __name__ == "__main__":
    main()
