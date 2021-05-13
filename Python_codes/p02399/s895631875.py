a, b = [int(x) for x in input().split() if x.isdigit()]
d = a // b
r = a % b
f = a / b
print('%s %s %.5f' % (d, r, f))