x, a, b = map(int, input().split())

x_a = abs(x-a)
x_b = abs(x-b)

if (x_a > x_b):
    print("B")

else:
    print("A")