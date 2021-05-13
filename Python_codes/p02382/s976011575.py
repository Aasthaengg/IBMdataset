n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x_minus_y = list(map(lambda xi, yi: xi - yi, x, y))

print(sum(list(map(abs, x_minus_y))))
print(sum(list(map(lambda x: x**2, x_minus_y))) ** .5)
print(sum(list(map(lambda x: abs(x)**3, x_minus_y))) ** (1 / 3))
print(max(list(map(abs, x_minus_y))))

