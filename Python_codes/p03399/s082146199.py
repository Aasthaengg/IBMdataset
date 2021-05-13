a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a >= b:
    train = b
elif a < b:
    train = a
if c >= d:
    bus = d
elif c < d:
    bus = c
print(train+bus)