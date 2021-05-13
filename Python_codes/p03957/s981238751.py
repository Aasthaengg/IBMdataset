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
    a = input()
    flg = 0
    for ele in a:
        if flg == 0 and ele == 'C':
            flg += 1
        if flg == 1 and ele == 'F':
            flg += 1
    if flg == 2:
        print('Yes')

    else:
        print('No')







if __name__ == '__main__':
    main()

