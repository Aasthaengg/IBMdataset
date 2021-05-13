# coding: utf-8

import sys
import math

import array
import bisect
import collections
from collections import Counter, defaultdict
import fractions
import heapq
import re

sys.setrecursionlimit(1000000)


def array2d(dim1, dim2, init=None):
    return [[init for _ in range(dim2)] for _ in range(dim1)]

def argsort(l, reverse=False):
    return sorted(range(len(l)), key=lambda i: l[i], reverse=reverse)

def argmin(l):
    return l.index(min(l))

def YESNO(ans, yes="YES", no="NO"):
    print([no, yes][ans])

II = lambda: int(input())
MI = lambda: map(int, input().split())
MIL = lambda: list(MI())
MIS = lambda: input().split()


def main():
    M, K = MI()

    if M == 1 and K == 1:
        return -1
    if K >= 2**M:
        return -1
    if K == 0:
        ans = []
        for i in range(0, 2**M):
            ans.append(i)
            ans.append(i)
        return " ".join(map(str, ans))

    ans = []
    ans.append(K)
    for i in range(0, 2**M):
        if i != K:
            ans.append(i)
    ans.append(K)
    for i in range(2**M - 1, -1, -1):
        if i != K:
            ans.append(i)
    return " ".join(map(str, ans))


if __name__ == "__main__":
    print(main())
