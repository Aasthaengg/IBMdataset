x = int(input())
a = int(input())
b = int(input())

x -= a
while True:
    if x >= b:
        x -= b
    else:
        break

print(x)