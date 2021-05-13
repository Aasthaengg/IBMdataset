#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	D
# CreatedDate:  2020-07-29 16:20:16 +0900
# LastModified: 2020-07-29 16:30:22 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from itertools import accumulate


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    s = [(x+1)/2 for x in p]
#    print(s)
    s = list(accumulate(s))
    s.insert(0, 0)
    ans = 0
#    print(s)
    for i in range(n-k+1):
        ans = max(ans, s[i+k]-s[i])
    print(ans)



if __name__ == "__main__":
    main()
