# -*- coding: utf-8 -*-
from functools import reduce

def mean_material(a, b):
    return (a+b)/2

n = int(input())
l_v = sorted(list(map(int, input().split())))

print(reduce(mean_material, l_v))
