import math

data = input().split()
a = int(data[0])
b = int(data[1])

d = math.floor(a/b)
r = a%b
f = round(a/b,5)

print(d, " ", r, " ", format(f,"f"))
