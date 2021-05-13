a, b = map(int, input().split())
total = 0
for _ in range(2):
    if a >= b:
        total = total + a
        a = a - 1
    else:
        total = total + b
        b = b - 1
print(total) 