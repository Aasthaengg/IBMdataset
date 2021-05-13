#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-08-08 22:05:18 +0900
# LastModified: 2020-08-09 00:49:47 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd
from math import sqrt


def prime_factor(n, prime_factor):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            prime_factor.append(i)

def main():
    n = int(input())
    prime_list = []
    prime_factor(n, prime_list)
    if not prime_list:
        print(n-1)
        return
    i = prime_list[-1]
    j = n//i
    print(i-1+j-1)



if __name__ == "__main__":
    main()
