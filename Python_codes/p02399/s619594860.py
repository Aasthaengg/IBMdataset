a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

print(str(d), str(r), str("%.8f" % f))