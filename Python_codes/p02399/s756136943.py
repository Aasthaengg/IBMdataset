a, b = map(int, input().split(" "))
d = a // b
r = a % b
f = "%.8f" % float(a / b)
print("{0} {1} {2}".format(d, r, f))