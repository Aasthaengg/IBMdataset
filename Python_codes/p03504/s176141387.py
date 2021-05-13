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
    num_bangumi, num_channel = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num_bangumi)]
    max_len = 10 ** 5 + 10

    ans_list = [[0 for i in range(max_len)] for j in range(num_channel)]

    for i in range(num_bangumi):
        s, t, c = data[i]
        ans_list[c - 1][s] += 1
        ans_list[c - 1][t] -= 1
    #
    # for i in range(num_channel):
    #     print(ans_list[i])
    # print()

    for i in range(num_channel):
        for j in range(1, max_len):
            if ans_list[i][j] == 1:
                ans_list[i][j - 1] += ans_list[i][j]
                ans_list[i][j] = 0

    # for i in range(num_channel):
    #     for j in range(max_len - 1)[::-1]:
    #         if ans_list[i][j] == -1:
    #             ans_list[i][j + 1] += ans_list[i][j]
    #             ans_list[i][j] = 0
    #
    # for i in range(num_channel):
    #     print(ans_list[i])
    #     print()



    ans = 0
    now_bangumi = 0

    for j in range(max_len):
        for i in range(num_channel):
            now_bangumi += ans_list[i][j]
        ans = max(ans, now_bangumi)

    print(ans)















if __name__ == '__main__':
    main()
