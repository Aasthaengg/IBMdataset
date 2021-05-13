import math

n = input()
a = map(float, raw_input().split(" "))
b = map(float, raw_input().split(" "))

p1 = sum([abs(x-y) for x, y in zip(a, b)])
p2 = math.sqrt(sum([(x - y)**2 for x, y in zip(a, b)]))
p3 = math.pow(sum([math.fabs(x - y)**3 for x, y in zip(a, b)]), (1.0/3.0))
p = max([abs(x - y) for x, y in zip(a, b)])

print "%f\n%f\n%f\n%f" % (p1, p2, p3, p)