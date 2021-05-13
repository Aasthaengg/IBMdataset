# -*- coding: utf-8 -*-
import numpy as np
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect


def zz():
    return list(map(int, input().split()))


def z():
    return int(input())


def S():
    return input()


def C(line):
    return [input() for _ in range(line)]


n = z()
v = zz()
a_lis = v[0::2]
b_lis = v[1::2]

a_all = [0]*(1 + 10**5)
b_all = [0]*(1 + 10**5)
for a in a_lis:
    a_all[a] += 1

for b in b_lis:
    b_all[b] += 1
nums = list(range(0, len(a_all)))
a_all = zip(a_all, nums)
b_all = zip(b_all, nums)
a_all = sorted(a_all, reverse=True)
b_all = sorted(b_all, reverse=True)

a_num_1, fixed_a_value = a_all[0]
b_num_1, fixed_b_value = b_all[0]
a_num_2 = a_num_1
b_num_2 = b_num_1
# print(a_num, b_num)
if (fixed_a_value == fixed_b_value):
    a_num_1, fixed_a_value = a_all[0]
    b_num_1, fixed_b_value = b_all[1]
    a_num_2, fixed_a_value = a_all[1]
    b_num_2, fixed_b_value = b_all[0]
# print(a_num, b_num)
ans = min(n-a_num_1-b_num_1, n-a_num_2-b_num_2)
print(ans)
