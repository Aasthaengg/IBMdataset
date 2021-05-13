import math

x = int(input())

ans = 1
for i in range(2, math.ceil(math.sqrt(x)) + 1):
    y = i * i
    while y <= x:
        ans = max(ans, y)
        y *= i
print(ans)
