a, b = map(int, input().split())

d = a // b
r = a % b
f = "{0:.5f}".format(a / b)

print(str(d) + " " + str(r) + " " + str(f))