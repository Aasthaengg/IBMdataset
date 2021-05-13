# from pprint import pprint
import math

# import collections

# n = int(input())
n, m = map(int, input().split(' '))
a = list(map(lambda x: int(x) * (-1), input().split(' ')))
# a = sorted(a, reverse=True)
# b = [math.log2(_a) for _a in a]


import heapq

q_a = heapq.heapify(a)

for m in range(m):
    x = heapq.heappop(a) * (-1)
    heapq.heappush(a, (x // 2) * (-1))

print(sum(a) * (-1))
