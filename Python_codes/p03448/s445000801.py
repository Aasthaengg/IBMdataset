#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/08
# Filename: main 
# Author: acto_mini

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    result = 0

    for i in range(A + 1):
        for j in range(B + 1):
            for k in range(C + 1):
                if (500 * i + 100 * j + 50 * k) == X:
                    result += 1
    print(result)
    return


if __name__ == '__main__':
    main()
