import math
n, k = map(int, input().split())
s = 0
for p in range(1, n+1):
    if k > p:
        m = math.ceil(math.log2(-(-k//p)))
        s += 0.5**m
    else:
        s += 1

print(s/n)
