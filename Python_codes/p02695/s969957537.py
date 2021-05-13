from sys import stdin
import sys
import math
from functools import reduce
import itertools

n, m, q = [int(x) for x in stdin.readline().rstrip().split()]

A = []
for i in range(q):
    A.append([int(x) for x in stdin.readline().rstrip().split()])

nums = [x for x in range(1,m+1)]

max_point = 0
for balls in itertools.combinations_with_replacement(nums, n):
    point = 0
    for i in range(q):
        if balls[A[i][1]-1] - balls[A[i][0]-1] == A[i][2]: point = point + A[i][3]
    max_point = max([max_point, point])

print(max_point)
