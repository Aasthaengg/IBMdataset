from sys import exit
n, a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

if (b - a) % 2 == 0:
    print((b - a) // 2)
    exit()

r = 0
to_wall_a = a - 1
to_wall_b = n - b

if to_wall_a <= to_wall_b:
    a = 1
    b -= to_wall_a
    r += to_wall_a

    b -= 1
    r += 1

    r += (b - a) // 2
else:
    b = n
    a += to_wall_b
    r += to_wall_b

    a += 1
    r += 1

    r += (b - a) // 2
print(r)