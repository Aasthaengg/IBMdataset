# -*- coding: utf-8 -*-
import sys
from sys import stdin

strN = stdin.readline().rstrip()
N = int(strN)
strLen = len(strN)

odd_count1 = 0
for i in range(1, strLen + 1):
    if i % 2 == 0:
        if i == strLen:
            print(odd_count1)
            sys.exit(0)
    else:
        if i == strLen:
            t1 = '1'
            t1 += '0' * (i - 1)
            t3 = N - int(t1) + 1
            odd_count1 += t3
            print(odd_count1)
            sys.exit(0)
        else:
            t1 = '1' + '0' * (i - 1)
            t2 = '9' * i
            odd_count1 += (int(t2) - int(t1)+1)
