a, b = [int(x) for x in input().split(' ')]

d = a // b
r = a % b
f = a / b

print("{0} {1} {2:.9f}".format(d, r, f))