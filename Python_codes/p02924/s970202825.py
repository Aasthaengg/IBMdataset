import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
from itertools import permutations,  combinations, accumulate
from functools import *
from collections import deque, defaultdict, Counter
from heapq import heapify, heappop, heappush, heappushpop

INF = float('inf')
NIL = - 1


# def gen_counter(stop=10):
#     index = 1
#     while True:
#         if stop < index:
#             break
#         yield index
#         index += 1


N = int(input())
res = (N - 1) * N // 2
print(res)


# arr = np.arange(1, N + 1)
# t_arr = np.append(arr[1:], arr[0])
# print(sum(arr % t_arr))

