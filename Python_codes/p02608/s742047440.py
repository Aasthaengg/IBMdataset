import math

n = int(input())
arr = [0] * n

for x in range(1,700):
    for y in range(1,700):
        for z in range(1,701):
            ans = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if ans <= n:
                arr[ans - 1] += 1

for i in range(n):
    print(arr[i])