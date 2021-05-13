import math

n = int(input())

x = list(map(int, input().split()))
y = list(map(int, input().split()))

one = sum(math.fabs(x[i] - y[i]) for i in range(n))
print("{0:5f}".format(one))

two = math.sqrt(sum((x[i] - y[i]) ** 2 for i in range(n)))
print("{0:5f}".format(two))

three = (sum(math.fabs((x[i] - y[i]) ** 3) for i in range(n))) ** (1/3)
print("{0:5f}".format(three))

inf = max(math.fabs(x[i] - y[i]) for i in range(n))
print("{0:5f}".format(inf))

