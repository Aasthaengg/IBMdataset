# coding=UTF-8
from collections import deque
from collections import Counter
from operator import itemgetter
from bisect import bisect_left, bisect
from decimal import *
import itertools
import sys
import math
import numpy as np
import time
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
    arr_sorted = sorted(arr, key=lambda x: x[1])

    now = 0

    for i in range(n):
        if now + arr_sorted[i][0] > arr_sorted[i][1]:
            print("No")
            return
        else:
            now += arr_sorted[i][0]
    print("Yes")


if __name__ == '__main__':
    main()
