n = int(input())
x = (1 + n) * n // 2
l = n // 3
x -= 3 * (1 + l) * l // 2
l = n // 5
x -= 5 * (1 + l) * l // 2
l = n // 15
x += 15 * (1 + l) * l // 2
print(x)