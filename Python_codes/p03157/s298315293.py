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

def check(x, y, now_add, color, high, width):
    global data
    move_dic = [(1, 0), (0, 1)]
    for move_x, move_y in move_dic:
        next_x = x + move_x
        next_y = y + move_y
        if 0 <= next_x < high and 0 <= next_y < width:
            if data[next_x][next_y] == 0:
                continue
            if data[next_x][next_y] != data[x][y]:
                now_add.add((i, j))
                color[data[next_x][next_y]] += 1
                check(next_x, next_y, now_add, color, high, width)


def main():
    high, width = map(int, input().split())
    data = [list(input()) for i in range(high)]

    ans = 0
    move_dic = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    for i in range(high):
        for j in range(width):
            if data[i][j] == 0:
                continue

            all_ele = set()
            now_ele = set()
            next_ele = set()
            count = defaultdict(int)

            now_ele.add((i, j))
            all_ele.add((i, j))
            count[data[i][j]] += 1

            while len(now_ele) > 0:
                for x, y in now_ele:
                    for move_x, move_y in move_dic:
                        next_x = x + move_x
                        next_y = y + move_y
                        if 0 <= next_x < high and 0 <= next_y < width:
                            if data[next_x][next_y] == 0 or (next_x, next_y) in all_ele:
                                continue
                            if data[next_x][next_y] != data[x][y]:
                                next_ele.add((next_x, next_y))
                                all_ele.add((next_x, next_y))
                                count[data[next_x][next_y]] += 1
                now_ele = next_ele
                next_ele = set()

            ans += count['.'] * count['#']
            for x, y in all_ele:
                data[x][y] = 0

    print(ans)




if __name__ == '__main__':
    main()
    # test()
