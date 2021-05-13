a, b = [int(x) for x in input().split()]
d = a // b
r = a % b
f = a / b
print('{0:d} {1:d} {2:f}'.format(d, r, f))