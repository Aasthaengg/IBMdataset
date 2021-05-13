from math import ceil

A, B = map(int, input().split())
result = ceil((B-1)/(A-1))
print(result)

