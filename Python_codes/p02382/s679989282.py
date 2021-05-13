n = int(input())
X = list(map(int,input().split()))
Y = list(map(int,input().split()))

x_y = []
for x, y in zip(X,Y):
    x_y.append(abs(x-y))

d1 = sum(x_y)
d2 = 0
for xy in x_y:
    d2 += xy ** 2
d2 = d2 ** (1/2)
d3 = 0
for xy in x_y:
    d3 += xy ** 3
d3 = d3 ** (1/3)
d4 = max(x_y)

print(d1)
print(d2)
print(d3)
print(d4)
