a, b = [int(x) for x in input().split() if x.isdigit()]
d = a // b
r = a % b
f = a / b
print("{0} {1} {2:.5f}".format(d, r, f))