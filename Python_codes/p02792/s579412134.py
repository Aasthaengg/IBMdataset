from collections import Counter, defaultdict
import sys

sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools
from copy import deepcopy
import queue
from collections import deque





def main():
    num = int(input())

    data = [[0 for i in range(10)] for j in range(10)]
    for i in range(1, num + 1):
        now_str = str(i)
        data[int(now_str[0])][int(now_str[-1])] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += data[i][j] * data[j][i]

    # print(data)
    print(ans)




if __name__ == '__main__':
    main()
