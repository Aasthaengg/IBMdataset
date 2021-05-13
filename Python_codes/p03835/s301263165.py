#! env python
# -*- coding: utf-8 -*-

import os
import sys


# ac_py.main
# Date: 2020/06/16
# Filename: main 
# Author: acto_mini

def main():
    K, S = map(int, input().split())

    ans = 0
    for i in range(K + 1):
        for j in range(K + 1):
            if 0 <= (S - i - j) <= K:
                ans += 1
    print(ans)
    return


if __name__ == '__main__':
    main()
