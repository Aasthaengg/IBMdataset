import math
n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

d1 = d2 = d3 = d4 = 0
l = []
for a, b in zip(a, b):
    d1 += math.pow(abs(a - b), 1)
    d2 += math.pow(abs(a - b), 2)
    d3 += math.pow(abs(a - b), 3)
    l.append(abs(a-b))

d1 = math.pow(d1, 1)
d2 = math.pow(d2, 1/2)
d3 = math.pow(d3, 1/3)
d4 = max(l)
print(d1)
print(d2)
print(d3)
print(d4)

