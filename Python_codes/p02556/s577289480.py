n = int(input())

x_plus_y = []
x_minus_y = []

for i in range(n):
    x, y = [int(_) for _ in input().split()]
    x_plus_y.append(x+y)
    x_minus_y.append(x-y)

x_plus_y.sort()
x_minus_y.sort()

print(max(x_plus_y[-1] - x_plus_y[0], x_minus_y[-1] - x_minus_y[0]))