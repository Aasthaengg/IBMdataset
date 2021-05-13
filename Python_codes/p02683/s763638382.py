import itertools
# import math
# import sys
import numpy as np

# K = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M, X = map(int, input().split())
# H = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort
# all_cases = list(itertools.permutations(P))
# a = list(itertools.combinations_with_replacement([i for i in range(1, M + 1)], N))
# print(a[0][0])
# print(conditions[0])

conditions = []
for i in range(N):
    CA = list(map(int, input().split()))
    conditions.append(CA)
conditions = np.array(conditions)
pattarns = list(itertools.product((0,1), repeat=N))

min_clear_cost = 10**20
for pattarn in pattarns:
    cost = 0
    A = np.zeros(M)
    for i, j in enumerate(pattarn):
        if j == 1:
            cost += conditions[i][0]
            A += conditions[i][1:]
    if min(A) >= X and min_clear_cost > cost:
        min_clear_cost = cost

if min_clear_cost == 10**20:
    min_clear_cost = -1

print(min_clear_cost)
