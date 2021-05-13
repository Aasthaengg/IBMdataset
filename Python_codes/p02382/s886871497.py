import math


n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

d1 = []
d2 = []
d3 = []
for i, j in zip(x, y):
    d1.append(abs(i - j))
    d2.append(abs(i - j)**2)
    d3.append(abs(i - j)**3)

print(sum(d1))
print(math.sqrt(sum(d2)))
print(sum(d3)**(1/3))
print(max(d1))


