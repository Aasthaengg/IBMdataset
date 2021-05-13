# import itertools
# import math
# import sys
# import numpy as np

N = int(input())
# S = input()
# n, *a = map(int, open(0))
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

d = {}
for i in range(N):
    S = input()
    d.setdefault(S, 0)
    d[S] += 1

cnt_max = max(d.values())
d = sorted(d.items(), key=lambda x:x[0]) # keyでsort

for k, v in d:
    if cnt_max == v:
        print(k)