n = int(input())
x = 0
y = 0
for i in range(n):
    a, b = input().split()
    if a > b:
        x += 3
    elif a < b:
        y += 3
    else:
        x += 1
        y += 1
print(x, y)
