# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]


K = z()
lunlun = [1, 2, 3, 4, 5, 6, 7, 8, 9]
if (K <= 9):
    print(lunlun[K-1])
    exit()
while len(lunlun) < K:
    for lun in lunlun:
        right = int(str(lun)[-1])
        if (right == 0):
            add = [0, 1]
        elif (right == 9):
            add = [8, 9]
        else:
            add = [right-1, right, right+1]
        for ad in add:
            # print(lun*10 + ad)
            lunlun.append(lun * 10 + ad)
        if (len(lunlun) >= K):
            break_flg = True
            break

# print(lunlun)
print(lunlun[K-1])
