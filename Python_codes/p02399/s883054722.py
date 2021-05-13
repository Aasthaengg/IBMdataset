(a, b) = (int(i) for i in input().split())
d = a // b
r = a % b
f = a / b

print('%s %s %.5f' % (d, r, f))