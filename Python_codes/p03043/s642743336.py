from math import *
n, k = map(int, input().split())
r = 0
for i in range(1, n + 1):
    if (i >= k):
        r += n + 1 - i
        break
    r += 1 / 2**ceil(log(k / i, 2))
print(r / n)
