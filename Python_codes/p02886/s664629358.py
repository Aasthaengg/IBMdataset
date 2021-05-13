# -*- coding: utf-8 -*-
from itertools import combinations

n = int(input())
d = list(map(int, input().split()))

pairs = combinations(d, 2)

print(sum(map(lambda x: x[0]*x[1], pairs)))
