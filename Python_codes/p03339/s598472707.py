#! env python
# -*- coding: utf-8 -*-

import os
import sys
from itertools import accumulate


# ac_py.main
# Date: 2020/06/14
# Filename: main 
# Author: acto_mini

def main():
    N = int(input())
    S = input()
    ans = 1000000000

    W = list()
    E = list()
    for i in range(N):
        flag = S[i] == "W"
        W.append(int(flag))
        E.append(int(not flag))

    #
    W_l = accumulate([0] + W[:-1])
    E_r = accumulate([0] + list(reversed(E[1:N])))

    for w, e in zip(W_l, reversed(list(E_r))):
        ans = min(ans, w + e)

    print(ans)
    return


if __name__ == '__main__':
    main()
