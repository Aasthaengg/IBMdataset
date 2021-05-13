#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# FileName: 	C
# CreatedDate:  2020-07-30 02:44:47 +0900
# LastModified: 2020-07-30 13:58:47 +0900
#


import os
import sys
# import numpy as np
# import pandas as pd


def main():
    n, m = map(int, input().split())
    switch_list = []
    for _ in range(m):
        command = list(map(int, input().split()))
        _ = command[0]
        switch_list.append(command[1:])
    p = list(map(int, input().split()))
    ans = 0
    for i in range(1 << n):
        flag = 1
        for j, switch in enumerate(switch_list):
            cnt = 0
            for s in switch:
                if 1 & i >> (s-1):
                    cnt += 1
            if cnt % 2 != p[j]:
                flag = 0
                break
        if flag == 1:
            ans += 1

    print(ans)






if __name__ == "__main__":
    main()
