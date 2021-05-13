#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	B
# CreatedDate:  2020-06-25 15:41:57 +0900
# LastModified: 2020-06-25 16:11:34 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    h, w = map(int, input().split())
    s = []
    s.append((w+2)*'.')
    for _ in range(h):
        s.append('.'+input()+'.')
    s.append((w+2)*'.')
#    print(s)
    cnt = [[0]*(w+2) for i in range(h+2)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if s[i][j] == '#':
                continue
            if s[i-1][j-1] == '#':
                cnt[i][j] += 1
            if s[i-1][j] == '#':
                cnt[i][j] += 1
            if s[i-1][j+1] == '#':
                cnt[i][j] += 1
            if s[i][j-1] == '#':
                cnt[i][j] += 1
            if s[i][j+1] == '#':
                cnt[i][j] += 1
            if s[i+1][j-1] == '#':
                cnt[i][j] += 1
            if s[i+1][j] == "#":
                cnt[i][j] += 1
            if s[i+1][j+1] == '#':
                cnt[i][j] += 1

    for i in range(1, h+1):
        for j in range(1, w+1):
            if s[i][j] == '#':
                print('#', end='')
                continue
            print(cnt[i][j], end='')
        print()






if __name__ == "__main__":
    main()
