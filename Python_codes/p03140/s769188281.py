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
    num = int(input())
    data = [input() for i in range(3)]

    ans = 0
    for i in range(num):
        aaa = set([data[0][i], data[1][i], data[2][i]])
        ans += len(aaa) - 1
    print(ans)



if __name__ == '__main__':
    main()
    # test()

