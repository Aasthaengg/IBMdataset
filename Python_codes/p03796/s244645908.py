#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    N = int(input())
    power = 1

    for i in range(N):
        power = power * (i + 1)
        power = power % (10 ** 9 + 7)

    print(power)
    return


if __name__ == '__main__':
    main()
