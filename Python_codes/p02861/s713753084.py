import itertools
import numpy as np
import math

n = int(input())
xy = []
for i in range(n):
    x, y = map(int, input().split())
    xy.append([x, y])

lis = [x for x in range(n)]

p_list = itertools.permutations(lis)

s = 0

for one_case in p_list:
    prev = 0
    for i in range(n):
        if i == 0:
            prev = one_case[0]
        else:
            s += np.sqrt((xy[one_case[i]][0] - xy[prev][0])**2 + (xy[one_case[i]][1] - xy[prev][1])**2)
            prev = one_case[i]
print(s/math.factorial(n))