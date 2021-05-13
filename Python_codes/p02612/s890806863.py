import math
n = int(input())
m = math.ceil(n / 1000) * 1000
print(m - n)