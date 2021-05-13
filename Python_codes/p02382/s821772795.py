import math
n = int(input())
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))

c = list(map(lambda x: abs(x[0]-x[1]), list(zip(a, b))))
print("{:.5f}".format(sum(c))) # 1

d = list(map(lambda x: x**2, c))
print("{:.5f}".format(math.sqrt(sum(d)))) # 2

e = list(map(lambda x: x**3, c))
print("{:.5f}".format(math.pow(sum(e), 1.0/3.0))) # 3

print("{:.5f}".format(max(c))) # inf