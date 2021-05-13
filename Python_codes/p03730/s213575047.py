#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    A, B, C = map(int, input().split())

    # if A % 2 != C % 2:
    #     print("NO")
    #     exit()

    for i in range(1, C*1000):
        if ((i * A) % B) == C:
            print("YES")
            break
    else:
        print("NO")

    return


if __name__ == '__main__':
    main()
