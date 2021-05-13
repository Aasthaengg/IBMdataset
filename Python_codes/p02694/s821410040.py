X = int(input())
i = 0
y = 100

while y < X:
    y += y // 100
    i += 1

print(i)
