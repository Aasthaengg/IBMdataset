x = raw_input().split()
a1 = int(x[0])
b1 = int(x[1])
a2 = float(x[0])
b2 = float(x[1])

p1 = a1 / b1
r = a1 % b1
p2 = a2 / b2

print u"%d %d %f" % (p1, r, p2)