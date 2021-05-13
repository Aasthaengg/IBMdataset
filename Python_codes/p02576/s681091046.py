import math
tmp = input().split(" ")
n = int(tmp[0])
x = int(tmp[1])
t = int(tmp[2])

print(math.ceil(n / x) * t)