from math import ceil
a, b = map(int, input().split())
ret = ceil((b-1)/(a-1))
print(ret)