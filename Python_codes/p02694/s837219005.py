x = int(input())
y = 100
year = 0

while y < x:
    y += int(y // 100)
    year += 1

print(year)