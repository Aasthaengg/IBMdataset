from statistics import mean
from math import ceil

# input
ab = list(map(int, input().split()))

print(ceil(mean(ab)))