a, b = map(int, input().split())
x = (a + b)/2
y = int(x)
if x-y == 0:
    print(int(x))
else:
    z = int(x) + 1
    print(z)