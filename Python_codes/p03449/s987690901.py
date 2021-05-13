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
    A = list()
    A.append(list(map(int, input().split())))
    A.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        p = 0
        k = 0
        for j in range(N):
            p += A[k][j]
            if i == j:
                k = 1
                p += A[k][j]
        ans = max(p, ans)

    print(ans)
    return


if __name__ == '__main__':
    main()
