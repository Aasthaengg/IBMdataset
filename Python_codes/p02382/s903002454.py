n = int(input())
x = map(int, input().split())
y = map(int, input().split())

x_y = [abs(xi - yi) for xi, yi in zip(x, y)]
p1 = sum(x_y)
p2 = sum(i ** 2 for i in x_y) ** (1 / 2)
p3 = sum(i ** 3 for i in x_y) ** (1 / 3)
p_inf = max(x_y)

print(p1)
print(p2)
print(p3)
print(p_inf)