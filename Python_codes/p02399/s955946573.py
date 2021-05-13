a, b = map(int, input().split())
d = a // b
r = a % b
f = round((a / b), 8)

print("{0} {1} {2:.5f}".format(d, r, f))