#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-07-29 14:22:57 +0900
# LastModified: 2020-07-29 14:45:16 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    R, G, B, N = map(int, input().split())
    r_max = N//R
    g_max = N//G
    b_max = N//B
    cnt = 0
    for r in range(r_max+1):
        ans = r*R
        for g in range((N-r*R)//G+1):
            ans += g*G
            if (N-ans)%B==0:
                cnt += 1
            ans = r*R
    print(cnt)





if __name__ == "__main__":
    main()
