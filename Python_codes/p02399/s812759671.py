a,b = map(int, raw_input().split(" "))
d = a / b
r = a % b
f = float(a) / float(b)
print "{0} {1} {2:.5f}".format(d, r, f)