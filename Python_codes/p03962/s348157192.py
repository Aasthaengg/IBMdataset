a, b, c = map(int, input().split())
d = a - b
e = b - c
f = c - a
if d != 0 and e != 0 and f != 0:
    print(3)
elif d == 0 and e != 0 and f != 0:
    print(2)
elif d != 0 and e == 0 and f != 0:
    print(2)
elif d != 0 and e != 0 and f == 0:
    print(2)
elif d == 0 and e == 0 and f == 0:
    print(1)