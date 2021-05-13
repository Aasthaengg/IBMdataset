a, b = map(str, input().split())

x = int(a * int(b))
y = int(b * int(a))

if x > y:
    print(x)
else:
    print(y)
