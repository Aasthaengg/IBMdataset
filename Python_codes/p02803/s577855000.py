from collections import Counter, defaultdict
import sys

sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
from copy import deepcopy
import queue
from collections import deque


def maxload(data_copy, i, j, high, width):
    data = deepcopy(data_copy)
    count = 0
    now_point = set()
    now_point.add((i, j))
    next_point = set()

    move = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    while len(now_point):
        for now_i, now_j in now_point:
            data[now_i][now_j] = count
            for move_i, move_j in move:
                next_i, next_j = now_i + move_i, now_j + move_j
                if next_i < 0 or next_i >= high or next_j < 0 or next_j >= width:
                    continue
                if data[next_i][next_j] != ".":
                    continue
                next_point.add((next_i, next_j))

        now_point = next_point
        next_point = set()
        count += 1

    return count - 1



def main():
    high, width = map(int, input().split())
    data = [list(input()) for i in range(high)]

    ans = 0

    for i in range(high):
        for j in range(width):
            if data[i][j] == "#":
                continue
            ans = max(ans, maxload(data, i, j, high, width))

    print(ans)


if __name__ == '__main__':
    main()
