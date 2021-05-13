from functools import reduce
N = int(input())
v = sorted([int(i) for i in input().split()])
print(reduce(lambda a, b:(a+b)/2, v))