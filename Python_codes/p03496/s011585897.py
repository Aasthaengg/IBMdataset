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
    data = list(map(int, input().split()))

    min_num = min(data)
    max_num = max(data)

    ans_list = []
    if max_num + min_num >= 0:
        idx = data.index(max_num)
        for i in range(num):
            if data[i] == max_num:
                continue
            ans_list.append([idx + 1, i + 1])
        for i in range(num - 1):
            ans_list.append([i + 1, i + 2])

    else:
        idx = data.index(min_num)
        for i in range(num):
            if data[i] == min_num:
                continue
            ans_list.append([idx + 1, i + 1])
        for i in range(num - 1)[::-1]:
            ans_list.append([i + 2, i + 1])

    print(len(ans_list))
    for i, j in ans_list:
        print(i, j)





if __name__ == '__main__':
    main()
