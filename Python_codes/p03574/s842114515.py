#! env python
# -*- coding: utf-8 -*-

import os
import sys
from itertools import repeat


# ac_py.main
# Date: 2020/06/13
# Filename: main 
# Author: acto_mini

def main():
    H, W = map(int, input().split())

    S = list()
    ans = list()

    for i in range(H):
        S.append(input())
        ans.append(list(repeat(0, W)))

    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                ans[i][j] = "#"

                # 左上
                if i > 0 and j > 0 and ans[i - 1][j - 1] != "#":
                    ans[i - 1][j - 1] += 1
                # 上
                if i > 0 and ans[i - 1][j] != "#":
                    ans[i - 1][j] += 1
                # 右上
                if i > 0 and j < W - 1 and ans[i - 1][j + 1] != "#":
                    ans[i - 1][j + 1] += 1

                # 左
                if j > 0 and ans[i][j - 1] != "#":
                    ans[i][j - 1] += 1
                # 右
                if j < (W - 1) and ans[i][j + 1] != "#":
                    ans[i][j + 1] += 1

                # 左下
                if i < (H - 1) and j > 0 and ans[i + 1][j - 1] != "#":
                    ans[i + 1][j - 1] += 1
                # 下
                if i < (H - 1) and ans[i + 1][j] != "#":
                    ans[i + 1][j] += 1
                # 右下
                if i < (H - 1) and j < W - 1 and ans[i + 1][j] != "#":
                    ans[i + 1][j + 1] += 1

    for i in range(H):
        print(*ans[i], sep="")
    return


if __name__ == '__main__':
    main()
