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
    data = list(map(int, input().split()))

    now_num = 10 ** 10
    ans = 0

    for i in range(num):
        if data[i] < now_num:
            now_num = data[i]
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
