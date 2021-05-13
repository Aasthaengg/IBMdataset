n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
p = 0
q = 0
p1 = 0
p2 = 0
p3 = 0
max = 0
import math
for i, j in zip(x, y):
    p1 += abs(i - j)
    p += abs((i - j) ** 2)
    p2 = math.sqrt(p)
    q += abs((i - j) ** 3)
    p3 = math.pow(q, 1.0/3.0)
    if abs(i - j) > max:
        max = abs(i - j)

print(p1)
print(p2)
print(p3)
print(max)