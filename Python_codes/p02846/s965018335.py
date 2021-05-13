from math import ceil
t1, t2 = map(int, input().split())
a1, a2 = map(int, input().split())
b1, b2 = map(int, input().split())
a = t1 * (a1 - b1)
b = t2 * (a2 - b2)
if a > 0:
    a *= -1
    b *= -1
if a + b < 0:
    print(0)
elif a + b > 0:
    if (-1 * a) % (a + b):
        print(((-1 * a) // (a + b)) * 2 + 1)
    else:
        print((-1 * a) // (a + b) * 2)
else:
    print("infinity")