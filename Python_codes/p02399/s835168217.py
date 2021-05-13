a, b = map(int, input().split())
d = int(a / b)
r = a % b
f = round(a / b, 6)
print("{} {} {:f}".format(d, r, f))
