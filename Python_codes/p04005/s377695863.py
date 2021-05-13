import math

a, b ,c = map(int, input().split())
lis = [a, b, c]
lis = sorted(lis)

t = lis[0] * lis[1]

b = math.ceil(lis[2]/2)
s = math.floor(lis[2]/2)

print(t*b - t*s)