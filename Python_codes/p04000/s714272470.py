from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
# from copy import deepcopy, copy

import queue
from collections import deque




def main():
    high, width, num = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num)]

    ans_list = defaultdict(int)
    move_dic = [-2, -1, 0]
    for i in range(num):
        a, b = data[i]
        a -= 1
        b -= 1
        for move_a in move_dic:
            for move_b in move_dic:
                now_a = a + move_a
                now_b = b + move_b
                if 0 <= now_a < high - 2 and 0 <= now_b < width - 2:
                    ans_list[(now_a, now_b)] += 1
        # print(ans_list)

    ans = Counter(list(ans_list.values()))
    print((high - 2) * (width - 2) - sum(list(ans.values())))
    for i in range(1, 10):
        print(ans[i])

if __name__ == '__main__':
    main()
