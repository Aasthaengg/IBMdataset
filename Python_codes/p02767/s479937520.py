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

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort

X = list(map(int, input().split()))

tots = []
for i in range(1, 101):
    tot = 0
    for j in X:
        tot += (j - i) ** 2
    tots.append(tot)

print(min(tots))