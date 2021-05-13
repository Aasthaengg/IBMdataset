import math
y = input().split()
t = int(y[0])
x = int(y[1])
a = math.floor((t/x) * 1000)
print(a / 1000)