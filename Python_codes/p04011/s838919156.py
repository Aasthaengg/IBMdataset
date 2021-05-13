a = int(input())
b = int(input())
c = int(input())
d = int(input())
x = 0
for i in range(a):
    if b > 0:
        x = x + c
        b = b - 1
    else:
        x = x + d
print(x)