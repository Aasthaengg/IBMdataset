# import itertools
# import math
# import sys
# import numpy as np

# K = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M = map(int, input().split())
H = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

flgs = [1] * N
for i in range(M):
    a, b = map(int, input().split())
    if H[a - 1] <= H[b - 1]:
        flgs[a - 1] = 0
    if H[a - 1] >= H[b - 1]:
        flgs[b - 1] = 0
print(sum(flgs))