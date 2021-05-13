from operator import mul
from functools import reduce

n = int(input())
a = list(map(int, input().split()))
k = [2 if i % 2 == 0 else 1 for i in a]

count = 3**len(a) - reduce(mul, k)

print(count)