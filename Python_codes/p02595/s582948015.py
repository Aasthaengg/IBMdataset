import math
n, d = map(int, input().split())
count = 0
for i in range(0,n):
    x, y = map(int, input().split())
    square = x * x + y * y
    distance = math.sqrt(square)
    if distance <= d:
        count += 1
print(count)