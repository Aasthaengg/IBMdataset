x1, y1, x2, y2 = list(map(int, input().split()))

a = x2 -x1
b = y2 -y1

b_v = a
a_v = -b
x3 = x2 + a_v
y3 = y2 + b_v

x4 = x3 -a
y4 = y3 -b
print(x3, y3, x4, y4)