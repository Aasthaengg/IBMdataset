from collections import Counter
from operator import mul
from functools import reduce

N = int(input())

line = [int(x) for x in input().split()]
counter = Counter(line)

collect = {key: int(value * (value - 1) / 2)
           for key, value in counter.items()}
min_collect = {key: int((value - 1) * (value - 2) / 2)
               for key, value in counter.items()}

max_value = sum(collect.values())

for i in line:
    print(min_collect[i] + max_value - collect[i])
