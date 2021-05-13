x = int(input())
a = int(input())
b = int(input())
x -= a
x -= b * (x // b)
print(x)