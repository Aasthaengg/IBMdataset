#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    a, b, x = map(int, input().split())

    print((b // x) - ((a - 1) // x))
    return


if __name__ == '__main__':
    main()
