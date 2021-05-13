n, a, b = map(int, input().split())
t = 1

while a != 0 and b != n + 1:
    if t:
        if a + 1 == b:
            a -= 1
        else:
            a += 1
    else:
        if b - 1 == a:
            b += 1
        else:
            b -= 1
    t ^= 1

print('Alice' if t else 'Borys')