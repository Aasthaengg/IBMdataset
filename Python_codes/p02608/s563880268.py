import math

n = int(input())
ans = [0]*n
root = n ** 0.5

for x in range(1, math.floor(root) + 1):
    for y in range(1, math.floor(root) + 1):
        for z in range(1, math.floor(root) + 1):
            result = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
            if result <= n:
                ans[result - 1] += 1

for num in ans:
    print(num)