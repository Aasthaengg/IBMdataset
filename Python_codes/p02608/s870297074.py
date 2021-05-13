import math

n = int(input())
res = [0] * 100000
count = 0
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            ans = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if ans > 10001:
                break
            if ans <= 10000:
                res[ans] += 1

for i in range(n):
    print(res[i + 1])