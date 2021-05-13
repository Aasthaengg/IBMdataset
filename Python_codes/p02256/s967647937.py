a = input().split()
x = int(a[0])
y = int(a[1])
while y:
    x, y = y, x%y
print(x)