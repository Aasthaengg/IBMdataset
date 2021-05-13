import copy
import math
import time
import statistics
import math
import itertools
import bisect
import sys
from decimal import *
from collections import deque


def get_int():
    return int(input())

def get_string():
    return input()

def get_int_list():
    return [int(x) for x in input().split()]

def get_string_list():
    return input().split()

def get_int_multi():
    return map(int, input().split())

def get_string_char_list():
    return list(str(input()))

# print("{} {}".format(a, b))
# a_list = [0] * a
sys.setrecursionlimit(10 ** 6)

def main():
    start = time.time()

    n = get_int()
    s = ""
    for _ in range(n):
        s += "ACL"

    print(s)


if __name__ == '__main__':
    main()