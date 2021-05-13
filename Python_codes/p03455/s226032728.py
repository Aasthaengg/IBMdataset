#! env python
# -*- coding: utf-8 -*-

import os
import sys

# ac_py.main.py
# Date: 2020/06/07
# Filename: main.py 

__author__ = 'acto_mini'
__date__ = "2020/06/07"


def main():
    a, b = map(int, input().split())
    if (a * b) % 2:
        print("Odd")
    else:
        print("Even")


if __name__ == '__main__':
    main()
