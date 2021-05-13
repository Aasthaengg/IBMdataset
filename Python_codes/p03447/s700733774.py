x = int(input())
a = int(input())
b = int(input())

if x - a >= 0:
    x = x - a

num = x // b
x = x - num * b
print(x)