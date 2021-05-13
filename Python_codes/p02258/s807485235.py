import math

n = int(input())
minv = int(input())
maxv = -math.pow(10, 9)

for _ in range(n-1):
    rt = int(input())
    maxv = max(maxv, rt - minv)
    minv = min(minv, rt)

print(maxv)