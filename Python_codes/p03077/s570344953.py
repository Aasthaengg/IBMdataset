import math
n = int(input())
tlist = [int(input()) for _ in range(5)]
s = min(tlist)
print(math.ceil(n/s) + 4)