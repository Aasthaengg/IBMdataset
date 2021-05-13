import math

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
a2 = (math.ceil(a / 10)) * 10
b2 = (math.ceil(b / 10)) * 10
c2 = (math.ceil(c / 10)) * 10
d2 = (math.ceil(d / 10)) * 10
e2 = (math.ceil(e / 10)) * 10
ls = [0 for i in range(5)]
ls[0] = a + b2 + c2 + d2 + e2
ls[1] = a2 + b + c2 + d2 + e2
ls[2] = a2 + b2 + c + d2 + e2
ls[3] = a2 + b2 + c2 + d + e2
ls[4] = a2 + b2 + c2 + d2 + e
print(min(ls))
