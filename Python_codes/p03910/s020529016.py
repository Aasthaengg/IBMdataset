import math

n = int(input())

k = math.ceil(((1 + 8 * n) ** 0.5 - 1) / 2)

tmp = k * (k + 1) / 2 - n
for i in range(1, k + 1):
    if i == tmp:
        continue
    print(i)