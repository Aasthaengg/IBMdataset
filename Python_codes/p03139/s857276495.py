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


def main():
    num, a, b = map(int, input().split())
    print(min(a, b), max(0, a + b - num))





if __name__ == '__main__':
    main()
    # test()

