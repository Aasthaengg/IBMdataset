#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-06-14 14:59:04 +0900
# LastModified: 2020-06-14 15:07:55 +0900
#


import os
import sys
#import numpy as np
#import pandas as pd
from itertools import accumulate as ac

def main():
    n,q = map(int,input().split())
    s = input()
    poly = [0]*len(s)
    for i in range(0,len(s)-1):
        if s[i]=='A' and s[i+1]=='C':
            poly[i]=1
    ans = list(ac(poly))
    ans.insert(0,0)
    for _ in range(q):
        l,r = map(int,input().split())
        print(ans[r-1]-ans[l-1])


if __name__ == "__main__":
    main()
