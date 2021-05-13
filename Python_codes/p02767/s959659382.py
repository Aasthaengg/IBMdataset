from sys import stdin
from math import ceil, floor
n = int(stdin.readline().rstrip())
data = [int(x) for x in stdin.readline().rstrip().split()]
m = sum(data) / len(data)
ceil_m = sum([(x-ceil(m))**2 for x in data])
floor_m = sum([(x-floor(m))**2 for x in data])
print(min(ceil_m, floor_m))
