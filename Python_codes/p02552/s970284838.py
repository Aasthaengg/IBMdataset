
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def array(size, init=0):
    return [[init for j in range(size[1])] for i in range(size[0])]


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())


x = II()

print((x+1) % 2)
