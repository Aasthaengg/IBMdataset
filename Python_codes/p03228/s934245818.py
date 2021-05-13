a, b, k = map(int, input().split())

for i in range(k):
    if i % 2 == 0:
        if a % 2 == 1:
            a -= 1
            a = 0.5 * a
            b += a
        elif a % 2 == 0:
            a = 0.5 * a
            b += a
    elif i % 2 == 1:
        if b % 2 == 1:
            b -= 1
            b = 0.5 * b
            a += b
        elif b % 2 == 0:
            b = 0.5 * b
            a += b

print(int(a), int(b))