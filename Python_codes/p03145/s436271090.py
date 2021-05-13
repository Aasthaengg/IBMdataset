from functools import reduce
from operator import mul

a, b, c = map(int, input().split())

print(reduce(mul, [a, b]) // 2)