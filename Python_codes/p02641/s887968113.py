# import itertools
# import math
# import sys
# import numpy as np

# K = int(input())
# S = input()
# n, *a = map(int, open(0))
X, N = map(int, input().split())
P = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

min_ = 999
num = 0
for i in range(102):
    if i in P:
        # print(i)
        continue
    _ = abs(i - X)
    if min_ > _:
        min_ = _
        num = i
print(num)