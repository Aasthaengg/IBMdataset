import math

input = map(float, raw_input().split(" "))
a = input[0]
b = input[1]
c = math.radians(input[2])

h = math.sin(c) * b
s = a * h / 2
l = math.pow((a - math.cos(c) * b) ** 2 + h ** 2, 0.5) + a + b

print "{0:.5f}".format(s)
print "{0:.5f}".format(l)
print "{0:.5f}".format(h)