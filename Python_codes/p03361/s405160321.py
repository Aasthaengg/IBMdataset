#! env python
# -*- coding: utf-8 -*-

import os
import sys

from itertools import repeat


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    H, W = map(int, input().split())

    S = list()

    for i in range(H):
        S.append(input())

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                # 上
                if i > 0 and S[i - 1][j] == "#":
                    continue
                # 左
                elif j > 0 and S[i][j - 1] == "#":
                    continue
                # 右
                elif j < (W - 1) and S[i][j + 1] == "#":
                    continue
                # 下
                elif i < (H - 1) and S[i + 1][j] == "#":
                    continue
                else:
                    print("No")
                    exit()

    print("Yes")
    return


if __name__ == '__main__':
    main()
