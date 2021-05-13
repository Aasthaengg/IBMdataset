#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    N, K = map(int, input().split())
    # all = K ** N
    # out_single, out_multi = 0, 0
    # for i in range(2, N + 1):
    #     out_multi += (N - i + 1) * K
    print(K * ((K - 1) ** (N - 1)))
    return


if __name__ == '__main__':
    main()
