a, b = map(int, input().split())
x = 0
y = 1
while y < b:
    y += (a - 1)
    x += 1

print(x)