#! env python
# -*- coding: utf-8 -*-

import os
import sys
import itertools


# atcoder.main
# Date: 2020/06/20
# Filename: main 
# Author: acto_mini

def splitter(str):
    for i in range(1, len(str)):
        start = str[0:i]
        end = str[i:]
        yield (start, end)
        for split in splitter(end):
            result = [start]
            result.extend(split)
            yield result


def main():
    S = input()
    A = list(splitter(S))

    ans = int(S)
    for i in range(len(A)):
        for j in range(len(A[i])):
            ans += int(A[i][j])

    print(ans)
    return


if __name__ == '__main__':
    main()
