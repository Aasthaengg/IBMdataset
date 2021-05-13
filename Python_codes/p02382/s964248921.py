import math
n = int(input())
x, y = [int(e) for e in input().split()], [int(e) for e in input().split()]
total_1 = total_2 = total_3 = total_max = 0
for x1, y1 in zip(x, y):
    total_1 += abs(x1 - y1)
    total_2 += (x1 - y1)**2
    total_3 += (abs(x1 - y1))**3
    if total_max < abs(x1 - y1):
        total_max = abs(x1 - y1)
print("{0:.5f}".format(total_1))
print("{0:.5f}".format(math.sqrt(total_2)))
print("{0:.5f}".format(math.pow(total_3, 1.0/3.0)))
print("{0:.5f}".format(total_max))

