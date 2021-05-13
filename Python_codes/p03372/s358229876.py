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
    num_sushi, length = map(int, input().split())
    data = [list(map(int, input().split())) for i in range(num_sushi)]

    ans = 0
    right1 = [0 for i in range(num_sushi)]
    right1_max = [0 for i in range(num_sushi)]
    for i in range(num_sushi):
        x, v = data[i]
        if i == 0:
            right1[i] = v - x
            right1_max[i] = max(0, right1[i])
        else:
            right1[i] = right1[i - 1] + v - (x - data[i - 1][0])
            right1_max[i] = max(right1_max[i - 1], right1[i])
        ans = max(ans, right1_max[i])

    left1 = [0 for i in range(num_sushi)]
    left1_max = [0 for i in range(num_sushi)]
    for i in range(num_sushi)[::-1]:
        x, v = data[i]
        x = length - x
        if i == num_sushi - 1:
            left1[i] = v - x
            left1_max[i] = max(0, left1[i])
        else:
            left1[i] = left1[i + 1] + v - (data[i + 1][0] - data[i][0])
            left1_max[i] = max(left1_max[i + 1], left1[i])
        ans = max(ans, left1_max[i])

    right2 = [0 for i in range(num_sushi)]
    for i in range(num_sushi - 1):
        x, v = data[i]
        if i == 0:
            right2[i] = v - 2 * x
        else:
            right2[i] = right2[i - 1] + v - 2 * (data[i][0] - data[i - 1][0])
        # print(right2, x, v, data)
        ans = max(ans, right2[i] + left1_max[i + 1])

    left2 = [0 for i in range(num_sushi)]
    for i in range(1, num_sushi)[::-1]:
        x, v = data[i]
        x = length - x
        if i == num_sushi - 1:
            left2[i] = v - 2 * x
        else:
            left2[i] = left2[i + 1] + v - 2 * (data[i + 1][0] - data[i][0])
        ans = max(ans, left2[i] + right1_max[i - 1])

    print(ans)









if __name__ == '__main__':
    main()
