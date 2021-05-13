n = int(input())
x = 0
for i in range(n - 1):
    x += int((n - 1) / (i + 1))
print(x)