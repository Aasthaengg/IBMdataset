import math

n, k = map(int, input().split())
a = math.ceil(n / k)
b = math.floor(n / k)
print(a - b)