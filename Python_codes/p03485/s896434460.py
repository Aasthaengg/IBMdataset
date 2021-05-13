a, b = map(int, input().split())
if (a + b) % 2 == 0:
    x = (a + b) / 2
else:
    x = (a + b + 1)/2
print(int(x))

