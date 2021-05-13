a, year = 100, 0
x = int(input())

while a < x:
    a += a // 100
    year += 1

print(year)