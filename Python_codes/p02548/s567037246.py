import math

n = int(input())
count = 0
for i0 in range(n):
    i0 += 1
    count += math.floor(n / i0)
    if n - (math.floor(n / i0) * i0) == 0:
        count -= 1
print(count)