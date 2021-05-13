from math import ceil
from functools import reduce
print(reduce(lambda x, y: int(ceil(x * 1.05 / 1000) * 1000) , [100000] + list(range(int(input())))))