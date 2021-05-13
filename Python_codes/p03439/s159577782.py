from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools


import queue
from collections import deque


def check(str0, left, right):

    if right - left <= 1:
        print(left)
        now_str = input()
        if now_str == 'Vacant':
            sys.exit()
        print(right)
        now_str = input()
        if now_str == 'Vacant':
            sys.exit()

    half = (left + right) // 2

    print(half)
    half_str = input()
    if half_str == 'Vacant':
        sys.exit()

    if (half_str == str0 and half % 2) or (half_str != str0 and half % 2 == 0):
        check(str0, left, half)
    else:
        check(str0, half, right)


def main():
    num = int(input())

    print(0)
    str0 = input()
    if str0 == 'Vacant':
        sys.exit()

    check(str0, 0, num)




if __name__ == '__main__':
    main()
