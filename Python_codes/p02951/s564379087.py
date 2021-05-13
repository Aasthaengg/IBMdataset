a = list(map(int, input().split()))
x = a[0]
y = a[1]
z = a[2]

if y + z > x:
    print(z-x+y)
else:
    print(0)