# 最短でも5分、んで最小値がボトルネック
from math import ceil
n = int(input())
minx = min([int(input()) for _ in range(5)])
print(4 + ceil(n / minx))
